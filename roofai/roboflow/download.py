from roboflow import Roboflow
import glob
from tqdm import tqdm

from blueness import module
from blue_options.elapsed_timer import ElapsedTimer
from blue_objects import objects

from roofai import NAME
from roofai.env import ROBOFLOW_API_KEY
from roofai.roboflow.create import create_project
from roofai.logger import logger


NAME = module.name(__file__, NAME)


# https://app.roboflow.com/kamangir/roof-dataset-one/1/export
def download_project(
    object_name: str,
    project_name: str,
    version: int,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.download_project: {}({}) -> {}".format(
            NAME,
            project_name,
            version,
            object_name,
        )
    )

    logger.info("🪄")

    return True
