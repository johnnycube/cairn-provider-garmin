# Cairn Garmin worker (Python)

Imports Garmin Connect activities and daily health metrics (HRV, sleep,
weight, steps, resting HR) into Cairn. Garmin has no public activity OAuth
API, so this uses the [`garminconnect`](https://pypi.org/project/garminconnect/)
library (Garth SSO with email/password).

It speaks Cairn's NATS control plane: serves `cairn.discover.garmin`, pulls
jobs from `cairn.jobs.*.garmin`, publishes protojson `cairn.worker.v1.JobResult`
to `cairn.results.*.garmin`, and heartbeats its capability manifest to the
`cairn_worker_presence` KV.

This is a **standalone repository** with no dependency on cairn-core. The only
contract it shares with the server is the proto messages (committed under
`proto/`) and the NATS subjects. Regenerate + recommit `proto/` from the Cairn
proto contract when it changes.

## Run (dev)

Dependencies are managed with [uv](https://docs.astral.sh/uv/) (`pyproject.toml`
+ `uv.lock`; Python version in `.python-version`).

```bash
uv sync --locked
export CAIRN_NATS_URL=nats://localhost:4222
export CAIRN_GARMIN_EMAIL=you@example.com   # dev fallback; prod creds come from the server
export CAIRN_GARMIN_PASSWORD=...
uv run python -m cairn_garmin.main
```

The generated proto stubs are loaded from `./proto` (override with
`CAIRN_PROTO_PATH`). `make check` runs lint, mypy strict, the tests with a
coverage floor, the dependency audit, the image build and fleetlint; see
[CONTRIBUTING.md](CONTRIBUTING.md) and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

### MFA accounts

The worker cannot answer an MFA prompt. Seed the Garth token store once with an
interactive login, then point the worker at it. Tokens live under
`$CAIRN_GARTH_HOME/<account_id>`, where `<account_id>` is the `account_id` the
server puts in that connection's jobs (`default` for the env-var dev fallback):

```bash
export CAIRN_GARMIN_EMAIL=you@example.com CAIRN_GARMIN_PASSWORD=...
uv run python -c "import os; from garminconnect import Garmin; g = Garmin(os.environ['CAIRN_GARMIN_EMAIL'], os.environ['CAIRN_GARMIN_PASSWORD'], prompt_mfa=lambda: input('MFA code: ')); g.login(); g.client.dump('/data/garth/<account_id>')"
```

The command prompts `MFA code:` on the terminal. Mount the resulting directory
into the container (the image sets `CAIRN_GARTH_HOME=/data/garth` and declares
`/data` as a volume); the worker resumes from the cached tokens and refreshes
them itself.

The image runs as the unprivileged user `cairn` (uid/gid 10001), so the token
directory must be readable and writable by that uid (`chown -R 10001:10001`, or
`fsGroup: 10001` in Kubernetes).

## Configuration

All settings are read from the environment in `cairn_garmin/config.py`.

| Variable | Default | Purpose |
| --- | --- | --- |
| `CAIRN_NATS_URL` | `nats://localhost:4222` | NATS server. |
| `CAIRN_NATS_USER` / `CAIRN_NATS_PASSWORD` | empty (anonymous) | NATS user/password auth. |
| `CAIRN_WORKER_NAME` | `garmin-fetcher` | Routing identity; must match the server-side enrollment name. Shared by all replicas. |
| `CAIRN_WORKER_INSTANCE_ID` | random 12-hex id | Per-replica presence key. Set to the pod name so a restart reuses its key. |
| `CAIRN_HEARTBEAT_INTERVAL_S` | `20` | Presence heartbeat interval. |
| `CAIRN_PULL_BATCH` | `4` | Jobs fetched per pull. |
| `CAIRN_GARMIN_EMAIL` / `CAIRN_GARMIN_PASSWORD` | empty | Dev fallback credentials, used only when a job carries no account. |
| `CAIRN_GARTH_HOME` | `~/.cache/cairn-garth` (`/data/garth` in the image) | Garth token store root; one subdirectory per account. |
| `CAIRN_PROTO_PATH` | `./proto` | Location of the generated proto stubs. |

Provider name (`garmin`), package and worker version are baked into
`config.py` and are not overridable; they define the worker's contract.

## What it does

Handlers in `cairn_garmin/runtime.py`:

- `discover` (request/reply on `cairn.discover.garmin`): paged activity listing
  for the server's Sync / Full-Sync.
- `fetch_source`: imports one activity (summary, and the sample stream when
  `fetch_streams` is set) and archives the raw response to the blob store.
- `reconcile`: lists activity since the watermark (bounded to 30 days), enqueues
  `fetch_source` for unknown activities, and publishes the new watermark to
  `cairn.results.reconcile.garmin.<account_id>`. Backlog jobs for the same
  account are coalesced within 10 minutes.
- `import_metrics`: daily HRV / Sleep / Weight / Steps / RestingHR as
  `ImportedMetric` events (the server persists them to `health_samples`).
  Trigger from the Connections UI ("Import health").
- `parse_blob`: re-maps an archived raw response with the current mapping
  logic, without calling Garmin.

Event-carrying results are claim-checked through the blob store; jobs that keep
failing are terminated after five deliveries with a failure envelope carrying
the real error.

Per-user credentials are delivered via `cairn.creds.garmin.get`. The capability
manifest advertises Activity, HRV, Sleep, Weight, Steps and RestingHR.

Field mapping (activity and health) is verified against a small set of live
activities; see `cairn_garmin/mapping.py` for observed quirks such as
duplicated stream timestamps on Zwift-synced rides.
