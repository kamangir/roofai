from blueness import module
from blue_options.elapsed_timer import ElapsedTimer

from roofai import NAME
from roofai.roboflow.create import create_project
from roofai.logger import logger


NAME = module.name(__file__, NAME)


def upload_to_project(
    object_name: str,
    project_name: str,
    create: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.upload_to_project: {} -> {}".format(
            NAME,
            object_name,
            project_name,
        )
    )

    if create:
        if not create_project(
            project_name=project_name,
            project_description="uploaded-from-{}".format(
                object_name.replace("_", "-")
            ),
            project_type="semantic-segmentation",
            project_license="MIT",
        ):
            return False

    timer = ElapsedTimer()

    logger.info("🪄")

    timer.stop()
    logger.info(f"took {timer.elapsed_pretty()}")

    return True
