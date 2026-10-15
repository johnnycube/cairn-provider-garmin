# Changelog

All notable changes to the Cairn Garmin worker are documented here. The format
follows [Keep a Changelog](https://keepachangelog.com/), and the project aims
to follow [Semantic Versioning](https://semver.org/). Dates are ISO-8601.

## [Unreleased]

## [0.2.3] — 2026-10-15

### Fixed
- A stream descriptor without `metricsIndex` no longer crashes the activity
  stream; the descriptor is skipped.

### Changed
- The image runs as the unprivileged user `cairn` (uid/gid 10001) instead of
  root. Only deployments that mount an existing `/data` volume written by the
  old image need to make it writable for that uid; otherwise cached Garmin
  tokens cannot be read.
- Dependencies are locked with uv (`pyproject.toml` + `uv.lock`); the image
  installs exactly the locked set. `requirements*.txt` are gone.
- Base images are pinned by digest; release images get commit-derived
  timestamps (`SOURCE_DATE_EPOCH`).
- The dev-fallback token store defaults to `~/.cache/cairn-garth` instead of
  `/tmp/cairn-garth`.
- The MFA seeding recipe uses garminconnect, since garminconnect 0.3 no longer
  depends on garth.
- `make check` gates CI and releases: ruff, mypy strict, tests with a coverage
  floor, pip-audit, licenses, gitleaks and the image build. CodeQL runs on
  pull requests.

## [0.2.2] — 2026-09-14

### Fixed
- Token persistence after a fresh login. garminconnect 0.3 renamed the
  `garth` client attribute to `client`, so the token dump raised and was
  silently swallowed; every job logged in to Garmin again. The worker now
  resolves either attribute and logs a warning if the write fails.
- Health-metric calls propagate authentication failures (401/403) instead of
  reporting an empty day; other per-metric errors are logged at debug.

### Changed
- README rewritten to match the code: full handler list (discover,
  fetch_source, reconcile, import_metrics, parse_blob), a configuration table
  with the real defaults, and the one-off Garth login recipe for MFA accounts.

### Removed
- The `Lap` capability from the manifest — the worker never emitted lap events.
- The unused `CAIRN_WORKER_ENROLLMENT_TOKEN` setting and the `nkeys`
  dependency; NATS auth is anonymous or user/password.

## [0.2.1] — 2026-09-11

### Changed
- Release images are signed keyless with cosign (Fulcio certificate bound to
  this repository's release workflow) and ship SLSA provenance and SBOM
  attestations; verify with `cosign verify` as documented in the workflow
  header. No functional change to the worker.
- GitHub Actions moved to the current majors of checkout, setup-python, and
  the docker build actions.

### Removed
- The Gitea mirror workflow — the repository is published from GitHub only.

## [0.2.0] — 2026-07-16

**First public release.** A standalone Python worker that imports Garmin
Connect activities and health metrics into
[Cairn](https://github.com/johnnycube/cairn-core), using the `garminconnect`
library (Garth SSO) since Garmin has no public activity OAuth API.

### Added
- Activity import: `discover` (paged listing) and `fetch_source` (one activity
  with its stream); reconcile jobs report a watermark and enqueue fetches for
  missing activities.
- Health metrics import (`import_metrics`): HRV, sleep, weight, steps, and
  resting heart rate as typed metric events.
- Cairn NATS control plane: job consumers on `cairn.jobs.*.garmin`, protojson
  `JobResult` publishing, capability-manifest heartbeats to the
  worker-presence KV.
- Claim-checked results with fail-fast failure envelopes carrying the true
  error reason.
- Per-user credentials delivered via the server credentials channel
  (`cairn.creds.garmin.get`); env-var credentials remain as a dev fallback.
- No dependency on cairn-core: the shared contract is the committed proto
  stubs under `proto/` plus the NATS subjects.

### Known limitations
- Some field mappings are lightly verified against the live Garmin API —
  expect minor key tweaks as real-world data surfaces edge cases.

## [0.1.0] — 2026-06-26

Initial development (internal pre-release iterations v0.1.0–v0.1.5).

[0.2.0]: https://github.com/johnnycube/cairn-provider-garmin/releases/tag/v0.2.0
