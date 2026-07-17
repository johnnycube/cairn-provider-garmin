# Cairn Garmin worker (Python)

Imports Garmin Connect activities (and, later, health metrics: HRV, sleep,
weight, steps, resting HR) into Cairn. Garmin has no public activity OAuth API,
so this uses the [`garminconnect`](https://pypi.org/project/garminconnect/)
library (Garth SSO with email/password).

It speaks Cairn's NATS control plane: pulls jobs from `cairn.jobs.*.garmin`,
publishes protojson `cairn.worker.v1.JobResult` to `cairn.results.fetch_source.garmin`,
and heartbeats its capability manifest to the `cairn_worker_presence` KV.

This is a **standalone repository** with no dependency on cairn-core. The only
contract it shares with the server is the proto messages (committed under
`proto/`) and the NATS subjects. Regenerate + recommit `proto/` from the Cairn
proto contract when it changes.

## Run (dev)

```bash
pip install -r requirements.txt
export CAIRN_NATS_URL=nats://localhost:4222
export CAIRN_GARMIN_EMAIL=you@example.com
export CAIRN_GARMIN_PASSWORD=...          # MFA accounts: seed the token store once
export PYTHONPATH=.                        # so `cairn_garmin` imports
python -m cairn_garmin.main
```

The generated proto stubs are loaded from `./proto` (override with
`CAIRN_PROTO_PATH`). Tests: `pip install -r requirements-dev.txt && pytest`.

## Status

- Activity import: `discover` (paged listing) + `fetch_source` (one activity,
  with stream). The server's Sync/Full-Sync drives both; no separate
  backfill/reconcile handler is needed (the server only enqueues `fetch_source`).
- Health metrics: `import_metrics` job → HRV/Sleep/Weight/Steps/RestingHR as
  `ImportedMetric` events (server persists them to `health_samples`, served at
  `/api/health`). Trigger from the Connections UI ("Import health").
- Per-user credentials delivered via `cairn.creds.garmin.get`
  (`CAIRN_GARMIN_EMAIL/PASSWORD` is a dev fallback only).
- Capability manifest advertised (Activity, Lap, HRV, Sleep, Weight, Steps,
  RestingHR).

### Follow-ups

- Field mapping (activity + health) is **unverified against the live Garmin API**
  — expect minor key tweaks on first real import.
- Production NATS enrollment-token + nkey auth (dev uses anonymous /
  `CAIRN_NATS_USER/PASSWORD`).
