"""Raw-blob archival: store the untouched Garmin response in object storage.

Mirrors the Strava worker — the server mints a presigned PUT
(cairn.blobs.presign_upload.garmin); we upload a self-describing JSON blob and
return its key as raw_blob_id. Best-effort: failures return None (import is
durable without the archive). Enables re-parse + raw viewing.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import logging
from datetime import datetime, timezone

import requests

from . import config as C

log = logging.getLogger("cairn.garmin")

ARCHIVE_VERSION = 1
PRESIGN_SUBJECT = f"cairn.blobs.presign_upload.{C.PROVIDER}"


async def archive(nc, user_id: str, source_id: str, activity: dict, details: dict | None) -> tuple[str | None, int]:
    body = json.dumps(
        {
            "version": ARCHIVE_VERSION,
            "provenance": {
                "provider": C.PROVIDER,
                "worker_name": C.WORKER_NAME,
                "worker_version": C.VERSION,
                "package": C.PACKAGE,
                "archived_at": datetime.now(timezone.utc).isoformat(),
            },
            "activity": activity,
            "details": details,
        }
    ).encode()

    try:
        reply = await nc.request(
            PRESIGN_SUBJECT,
            json.dumps(
                {
                    "user_id": user_id,
                    "source_id": source_id,
                    "provider": C.PROVIDER,
                    "content_type": "application/json",
                    "content_length": len(body),
                }
            ).encode(),
            timeout=10,
        )
        up = json.loads(reply.data)
    except Exception as e:  # noqa: BLE001
        log.warning("presign failed: %s", e)
        return None, 0
    if up.get("error") or not up.get("url"):
        log.warning("presign rejected: %s", up.get("error"))
        return None, 0

    method = up.get("method") or "PUT"
    headers = dict(up.get("required_headers") or {})
    headers.setdefault("Content-Type", "application/json")
    try:
        resp = await asyncio.to_thread(
            requests.request, method, up["url"], data=body, headers=headers, timeout=30
        )
    except Exception as e:  # noqa: BLE001
        log.warning("blob upload failed: %s", e)
        return None, 0
    if not (200 <= resp.status_code < 300):
        log.warning("blob upload status %s", resp.status_code)
        return None, 0
    return (up.get("blob_id") or None), len(body)


async def upload_result(nc, body: bytes) -> dict:
    """Claim-check upload for an event-carrying JobResult (kind "result" →
    short-lived transfer/ key, deleted by the server after ingest). NOT
    best-effort like archive(): a lost result body means a lost import, so
    failures raise and the job NAKs/retries.
    """
    sha = hashlib.sha256(body).hexdigest()
    reply = await nc.request(
        PRESIGN_SUBJECT,
        json.dumps(
            {
                "provider": C.PROVIDER,
                "kind": "result",
                "content_type": "application/json",
                "content_length": len(body),
                "content_sha256": sha,
            }
        ).encode(),
        timeout=10,
    )
    up = json.loads(reply.data)
    if up.get("error") or not up.get("url"):
        raise RuntimeError(f"result presign rejected: {up.get('error')}")

    method = up.get("method") or "PUT"
    headers = dict(up.get("required_headers") or {})
    headers.setdefault("Content-Type", "application/json")
    resp = await asyncio.to_thread(
        requests.request, method, up["url"], data=body, headers=headers, timeout=30
    )
    if not (200 <= resp.status_code < 300):
        raise RuntimeError(f"result upload status {resp.status_code}")
    return {"blob_id": up.get("blob_id") or "", "size": len(body), "sha256": sha}


async def _presign_download(nc, blob_id: str) -> str | None:
    try:
        reply = await nc.request(
            C.PRESIGN_DOWNLOAD_SUBJECT,
            json.dumps({"blob_id": blob_id}).encode(),
            timeout=10,
        )
        up = json.loads(reply.data)
    except Exception as e:  # noqa: BLE001
        log.warning("presign download failed: %s", e)
        return None
    if up.get("error") or not up.get("url"):
        return None
    return up["url"]


async def fetch(nc, url: str, fallback_handle: str) -> dict:
    """Download + decode an archived envelope, re-presigning from the stored
    blob key if the supplied URL is missing or expired. Returns the decoded
    {version, provenance, activity, details} dict.
    """
    async def _get(u: str):
        return await asyncio.to_thread(requests.get, u, timeout=30)

    resp = None
    if url:
        try:
            resp = await _get(url)
        except Exception as e:  # noqa: BLE001
            log.warning("blob GET failed, will re-presign: %s", e)
            resp = None
    if (resp is None or resp.status_code >= 400) and fallback_handle:
        fresh = await _presign_download(nc, fallback_handle)
        if not fresh:
            raise RuntimeError("could not presign archived blob")
        resp = await _get(fresh)
    if resp is None:
        raise RuntimeError("no usable blob URL")
    if not (200 <= resp.status_code < 300):
        raise RuntimeError(f"blob GET status {resp.status_code}")
    return json.loads(resp.content)
