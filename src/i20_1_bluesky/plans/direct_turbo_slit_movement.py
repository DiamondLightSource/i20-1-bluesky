from typing import Any, List

import bluesky.plan_stubs as bps
from dodal.common.types import MsgGenerator

# from dls_bluesky_core.core import in_micros
# from dodal.common.types import MsgGenerator
# from ophyd_async.core import (
#     AsyncStatus,
#     DetectorTrigger,
#     HardwareTriggeredFlyable,
#     wait_for_value,
# )
# from ophyd_async.core.flyer import TriggerInfo, TriggerLogic
# from ophyd_async.panda import (
#     PandA,
#     SeqTableRow,
#     seq_table_from_rows,
# )
# from dodal.devices.turbo_slit import TurboSlit


# https://github.com/DiamondLightSource/i22-bluesky/blob/DAQ-5039/src/i22_bluesky/plans/fly_collect.py
# todo appears that we need to emulate this. Or maybe that's for the more complex plan,
# with triggers
# it uses SeqBlock https://github.com/bluesky/ophyd-async/blob/main/src/ophyd_async/panda/_common_blocks.py
# ? zebra? or only panda hopefully
# xpress 3


def continuous_movement(motors: List[Any] = None, devices: List[Any] = None) -> MsgGenerator:
    yield from bps.stage_all(*devices)
    yield from bps.open_run()
    pass
    print("empty run")
    # yield from prepare_all_with_trigger(flyer, devices, batches)
    # yield from fly_and_collect(flyer, devices)
    yield from bps.close_run()
    yield from bps.unstage_all(*devices)
