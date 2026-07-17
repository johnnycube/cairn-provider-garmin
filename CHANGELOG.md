# Changelog

All notable changes to the Cairn Garmin worker are documented here. The format
follows [Keep a Changelog](https://keepachangelog.com/), and the project aims
to follow [Semantic Versioning](https://semver.org/). Dates are ISO-8601.

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
