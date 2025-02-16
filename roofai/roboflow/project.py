from roboflow import Roboflow

from blueness import module
from blue_options.elapsed_timer import ElapsedTimer

from roofai import NAME
from roofai.env import ROBOFLOW_API_KEY
from roofai.logger import logger


NAME = module.name(__file__, NAME)

list_of_project_types = [
    "object-detection",
    "single-label-classification",
    "multi-label-classification",
    "instance-segmentation",
    "semantic-segmentation",
]


def create_project(
    project_name: str,
    project_description: str,
    project_type: str = "semantic-segmentation",
    project_license: str = "MIT",
) -> bool:
    if project_type not in list_of_project_types:
        logger.error(f"{project_type}: project type not found.")
        return False

    logger.info(
        "{}.create_project({}/{}): {}".format(
            NAME,
            project_type,
            project_name,
            project_description,
        )
    )

    timer = ElapsedTimer()
    try:
        rf = Roboflow(api_key=ROBOFLOW_API_KEY)

        _ = rf.workspace().create_project(
            project_name=project_name,
            project_license=project_license,
            project_type=project_type,
            annotation=project_description,
        )
    except Exception as e:
        logger.error(e)
        return False

    timer.stop()
    logger.info(f"took {timer.elapsed_pretty()}")

    return True
