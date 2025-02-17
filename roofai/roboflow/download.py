import os
from roboflow import Roboflow
from tqdm import tqdm
import glob
import matplotlib.pyplot as plt
import numpy as np

from blueness import module
from blue_options.elapsed_timer import ElapsedTimer
from blue_objects import objects, path, file
from blue_objects.metadata import post_to_object

from roofai import NAME, fullname
from roofai.env import ROBOFLOW_API_KEY
from roofai.logger import logger


NAME = module.name(__file__, NAME)


# https://app.roboflow.com/kamangir/roof-dataset-one/1/export
def download_project(
    object_name: str,
    project_name: str,
    project_version: int,
    clean: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.download_project: {}({}) -> {}{}".format(
            NAME,
            project_name,
            project_version,
            object_name,
            " clean" if clean else "",
        )
    )

    metadata = {
        "input": {
            "project": project_name,
            "version": project_version,
        }
    }

    object_path = objects.object_path(object_name)
    temp_path = os.path.join(
        object_path,
        "downloaded_from_roboflow",
    )
    if not path.create(temp_path, log=verbose):
        return False

    timer = ElapsedTimer()

    try:
        rf = Roboflow(api_key=ROBOFLOW_API_KEY)

        project = rf.workspace().project(project_name)

        version = project.version(project_version)

        _ = version.download(
            model_format="png-mask-semantic",
            location=temp_path,
            overwrite=True,
        )
    except Exception as e:
        logger.error(e)
        return False

    timer.stop()
    logger.info(f"took {timer.elapsed_pretty()}")

    success, classes_df = file.load_dataframe(
        os.path.join(temp_path, "train/_classes.csv"),
        log=verbose,
    )
    if not success:
        return False

    list_of_classes = [
        class_name.strip() for class_name in classes_df[" Class"].tolist()
    ]
    logger.info(
        "{} class(es): {}".format(
            len(list_of_classes),
            ", ".join(list_of_classes),
        )
    )

    for image_filename in tqdm(
        glob.glob(
            os.path.join(
                temp_path,
                "train/*.jpg",
            )
        )
    ):
        record_id = file.name(image_filename).replace(".", "-")
        logger.info(record_id)

        success, image = file.load_image(
            image_filename,
            log=verbose,
        )
        if not success:
            return False
        if not file.save_image(
            os.path.join(
                object_path,
                f"SegNet-Tutorial/CamVid/train/{record_id}.png",
            ),
            image,
            log=verbose,
        ):
            return False

        mask_filename = os.path.join(
            file.path(image_filename),
            "{}_mask.png".format(
                file.name(image_filename),
            ),
        )

        success, mask = file.load_image(
            mask_filename,
            log=verbose,
        )
        if not success:
            return False
        if not file.save_image(
            os.path.join(
                object_path,
                f"SegNet-Tutorial/CamVid/trainannot/{record_id}.png",
            ),
            mask,
            log=verbose,
        ):
            return False

        if not file.save_image(
            os.path.join(
                object_path,
                f"SegNet-Tutorial/CamVid/traina-colored/{record_id}.png",
            ),
            (
                plt.cm.viridis(mask[:, :, 0].astype(np.float32) / len(list_of_classes))
                * 255
            ).astype(np.uint8)[:, :, :3],
            log=verbose,
        ):
            return False

        if clean and not all(
            file.delete(filename_)
            for filename_ in [
                image_filename,
                mask_filename,
            ]
        ):
            return False

    if not file.save_yaml(
        os.path.join(object_path, "metadata.yaml"),
        {
            "classes": list_of_classes,
            "ingested-by": fullname(),
            "kind": "CamVid",
            "source": "gmaps",
        },
        log=True,
    ):
        return False

    return post_to_object(
        object_name,
        NAME.replace(".", "-"),
        metadata,
    )
