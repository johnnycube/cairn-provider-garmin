"""Cairn Garmin worker.

Bootstraps the committed proto stubs (./proto) onto sys.path so
`cairn.worker.v1` / `cairn.v1` import. Override with CAIRN_PROTO_PATH;
defaults to the in-repo location. The stubs are generated from the Cairn
proto contract and committed here — this worker has no dependency on
cairn-core; the contract is the proto messages plus the NATS subjects.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

_default = Path(__file__).resolve().parents[1] / "proto"
_proto_path = os.getenv("CAIRN_PROTO_PATH", str(_default))
if _proto_path not in sys.path:
    sys.path.insert(0, _proto_path)
