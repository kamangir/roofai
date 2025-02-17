from typing import Tuple, Any
from roboflow import Roboflow
import pprint

from blueness import module
from blue_options.elapsed_timer import ElapsedTimer

from roofai import NAME
from roofai.env import ROBOFLOW_API_KEY
from roofai.logger import logger


NAME = module.name(__file__, NAME)


def get_status() -> Tuple[bool, Any]:
    rf = Roboflow(api_key=ROBOFLOW_API_KEY)

    try:
        status = rf.workspace()
    except Exception as e:
        logger.error(e)
        return False, {}

    print(status)

    return True, status
