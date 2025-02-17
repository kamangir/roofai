import os
from roboflow import Roboflow

from blueness import module
from blue_options.elapsed_timer import ElapsedTimer
from blue_objects import objects, path
from blue_objects.metadata import post_to_object

from roofai import NAME
from roofai.env import ROBOFLOW_API_KEY
from roofai.logger import logger


NAME = module.name(__file__, NAME)


# https://app.roboflow.com/kamangir/roof-dataset-one/1/export
def download_project(
    object_name: str,
    project_name: str,
    project_version: int,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.download_project: {}({}) -> {}".format(
            NAME,
            project_name,
            project_version,
            object_name,
        )
    )

    metadata = {
        "input": {
            "project": project_name,
            "version": project_version,
        }
    }

    temp_folder = os.path.join(
        objects.object_path(object_name),
        "downloaded_from_roboflow",
    )
    if not path.create(temp_folder, log=True):
        return False

    timer = ElapsedTimer()

    try:
        rf = Roboflow(api_key=ROBOFLOW_API_KEY)

        project = rf.workspace().project(project_name)

        version = project.version(project_version)

        _ = version.download(
            model_format="png-mask-semantic",
            location=temp_folder,
            overwrite=True,
        )
    except Exception as e:
        logger.error(e)
        return False

    timer.stop()
    logger.info(f"took {timer.elapsed_pretty()}")

    return post_to_object(
        object_name,
        NAME.replace(".", "-"),
        metadata,
    )
