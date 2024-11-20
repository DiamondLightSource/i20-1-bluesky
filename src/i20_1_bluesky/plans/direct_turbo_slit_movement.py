from typing import Any

import bluesky.plan_stubs as bps
from dodal.common.types import MsgGenerator


def continuous_movement(
    motors: list[Any] | None = None, devices: list[Any] | None = None
) -> MsgGenerator:
    if motors is None:
        motors = []
    if devices is None:
        devices = []
    yield from bps.stage_all(*devices)
    yield from bps.open_run()
    print("empty run")
    yield from bps.close_run()
    yield from bps.unstage_all(*devices)
