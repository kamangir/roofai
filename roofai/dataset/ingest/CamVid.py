import os

from blue_objects import file

from roofai import NAME, VERSION
from roofai.logger import logger

CLASSES = [
    "sky",
    "building",
    "pole",
    "road",
    "pavement",
    "tree",
    "signsymbol",
    "fence",
    "car",
    "pedestrian",
    "bicyclist",
    "unlabelled",
]


def ingest_CamVid(output_dataset_path: str) -> bool:
    logger.info(f"ingesting CamVid -> {output_dataset_path}")

    return file.save_yaml(
        os.path.join(output_dataset_path, "metadata.yaml"),
        {
            "classes": CLASSES,
            "kind": "CamVid",
            "source": "CamVid",
            "ingested-by": f"{NAME}-{VERSION}",
        },
        log=True,
    )
