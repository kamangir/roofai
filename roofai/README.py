import os

from blue_objects import file, README

from roofai import NAME, VERSION, ICON, REPO_NAME
from roofai.dataset.README import items as dataset_items


items = README.Items(
    [
        {
            "name": "datasets",
            "url": "./roofai/dataset",
            "marquee": "https://github.com/kamangir/assets/blob/main/roofAI/AIRS-cache-v45--review-index-2.png?raw=true",
            "description": "Semantic Segmentation Datasets",
        },
        {
            "name": "semseg",
            "url": "./roofai/semseg",
            "marquee": "./assets/predict-00247.png",
            "description": "A Semantic Segmenter based on [segmentation_models.pytorch](<https://github.com/qubvel/segmentation_models.pytorch/blob/master/examples/cars%20segmentation%20(camvid).ipynb>).",
        },
    ]
)


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            cols=readme.get("cols", 3),
            path=os.path.join(file.path(__file__), readme["path"]),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
        )
        for readme in [
            {
                "items": items,
                "path": "..",
            },
            {
                "items": dataset_items,
                "cols": len(dataset_items),
                "path": "dataset",
            },
            {
                "path": "semseg",
            },
        ]
    )
