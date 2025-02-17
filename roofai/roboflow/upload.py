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


# https://docs.roboflow.com/api-reference/images/upload-api
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

    rf = Roboflow(api_key=ROBOFLOW_API_KEY)
    project = rf.workspace().project(project_name)

    for filename in tqdm(
        glob.glob(
            objects.path_of(
                object_name=object_name,
                filename="*.png",
            )
        )
    ):
        logger.info(filename)

        try:
            project.upload(
                image_path=filename,
                batch_name=object_name,
                split="train",
                num_retry_uploads=3,
                # sequence_number=99,
                # sequence_size=100,
            )

        # - sequence_number: [Optional] If you want to keep the order of your images in the dataset, pass sequence_number and sequence_size..
        # - sequence_size: [Optional] The total number of images in the sequence. Defaults to 100,000 if not set.

        except Exception as e:
            logger.error(e)
            return False

    timer.stop()
    logger.info(f"took {timer.elapsed_pretty()}")

    return True
