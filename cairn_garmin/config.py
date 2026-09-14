"""Worker configuration from environment."""
from __future__ import annotations

import os
import uuid
from dataclasses import dataclass, field

# PROVIDER + PACKAGE + VERSION are compile-time identity: with the capability
# manifest they define this worker's schema/contract, so they are baked into the
# source (NOT env-overridable). Bump VERSION here when the worker's output shape
# changes.
PROVIDER = "garmin"
PACKAGE = "cairn.workers.garmin"
VERSION = "1"

# WORKER_NAME is the admin-defined routing identity (it must match the
# enrollment name) and is SHARED across every instance of this worker — so it is
# env-configurable, defaulting to "garmin-fetcher". Distinct from instance_id
# (below), which is per-instance.
WORKER_NAME = os.getenv("CAIRN_WORKER_NAME", "garmin-fetcher")

JOB_STREAM = "CAIRN_JOBS"
RESULT_SUBJECT = f"cairn.results.fetch_source.{PROVIDER}"
RESULT_METRICS = f"cairn.results.import_metrics.{PROVIDER}"
SUBJ_FETCH = f"cairn.jobs.fetch_source.{PROVIDER}"
SUBJ_METRICS = f"cairn.jobs.import_metrics.{PROVIDER}"
SUBJ_PARSE_BLOB = f"cairn.jobs.parse_blob.{PROVIDER}"
SUBJ_RECONCILE = f"cairn.jobs.reconcile.{PROVIDER}"
# Reconcile results are account-suffixed so the server can attribute the
# watermark: cairn.results.reconcile.garmin.<external_account_id>.
RESULT_RECONCILE_PREFIX = f"cairn.results.reconcile.{PROVIDER}"
PRESIGN_DOWNLOAD_SUBJECT = f"cairn.blobs.presign_download.{PROVIDER}"
PRESENCE_KV = "cairn_worker_presence"


@dataclass
class Config:
    nats_url: str = field(default_factory=lambda: os.getenv("CAIRN_NATS_URL", "nats://localhost:4222"))
    # Per-instance id, only needs to be UNIQUE per running instance (it
    # disambiguates replicas of the same WORKER_NAME in presence/heartbeats).
    # Unset → a random uuid is generated; in k8s set it to the pod name so a
    # restart reuses the same presence key instead of leaving a ghost.
    instance_id: str = field(default_factory=lambda: os.getenv("CAIRN_WORKER_INSTANCE_ID", "") or uuid.uuid4().hex[:12])
    nats_user: str = field(default_factory=lambda: os.getenv("CAIRN_NATS_USER", ""))
    nats_password: str = field(default_factory=lambda: os.getenv("CAIRN_NATS_PASSWORD", ""))
    heartbeat_interval_s: int = field(default_factory=lambda: int(os.getenv("CAIRN_HEARTBEAT_INTERVAL_S", "20")))
    pull_batch: int = field(default_factory=lambda: int(os.getenv("CAIRN_PULL_BATCH", "4")))

    # Dev fallback Garmin credentials when the job carries none (single account).
    garmin_email: str = field(default_factory=lambda: os.getenv("CAIRN_GARMIN_EMAIL", ""))
    garmin_password: str = field(default_factory=lambda: os.getenv("CAIRN_GARMIN_PASSWORD", ""))
    # Garth token store dir (persists Garmin session so we don't log in every job).
    garth_home: str = field(default_factory=lambda: os.getenv("CAIRN_GARTH_HOME", "/tmp/cairn-garth"))


def load() -> Config:
    return Config()
