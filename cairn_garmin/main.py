"""Entrypoint for the Cairn Garmin worker."""

from __future__ import annotations

import asyncio
import logging
import signal

from . import config as C
from .runtime import Worker


async def _main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    cfg = C.load()
    # Credentials are fetched per account via cairn.creds.garmin.get; the env
    # values are only a single-account dev fallback.
    worker = Worker(cfg)

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, worker.stop)
    await worker.run()


def main() -> None:
    asyncio.run(_main())


if __name__ == "__main__":
    main()
