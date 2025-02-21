import os

from blue_options.help.functions import get_help
from blue_objects import file, README
from blue_objects.env import abcli_path_git

from roofai import NAME, VERSION, ICON, REPO_NAME
from roofai.help.functions import help_functions
from roofai.dataset.README import items as dataset_items


items = README.Items(
    [
        {
            "name": "Datasets",
            "url": "./roofai/dataset",
            "marquee": "https://github.com/kamangir/assets/blob/main/roofAI/AIRS-cache-v45--review-index-2.png?raw=true",
            "description": "Semantic Segmentation Datasets",
        },
        {
            "name": "Semantic Segmentation (SemSeg)",
            "url": "./roofai/semseg",
            "marquee": "./assets/predict-00247.png",
            "description": "A Semantic Segmenter based on [segmentation_models.pytorch](<https://github.com/qubvel/segmentation_models.pytorch/blob/master/examples/cars%20segmentation%20(camvid).ipynb>).",
        },
        {
            "name": "Google Maps API",
            "url": "./roofai/google_maps/api",
            "marquee": "https://github.com/kamangir/assets/blob/main/static-image-api-2025-02-15-wnfsd9/static-image-api-2025-02-15-wnfsd9-2X.gif?raw=true",
            "description": "Integrations with the Google Maps [Static](https://developers.google.com/maps/documentation/maps-static/start) and [Geocoding](https://developers.google.com/maps/documentation/geocoding/start) APIs.",
        },
        {
            "name": "SemSeg on Google Maps",
            "url": "./roofai/google_maps/semseg",
            "marquee": "https://github.com/kamangir/assets/raw/main/roofAI/roboflow/labelling-2.png?raw=true",
            "description": "Google Maps semantic segmentation datasets and models.",
        },
        {},
        {
            "name": "Google Earth API",
            "url": "./roofai/google_earth",
            "marquee": "https://github.com/kamangir/assets/raw/main/roofAI/google_earth/glb-viewer.png?raw=true",
            "description": "Integration with the [Google Photorealistic 3D Tiles](https://developers.google.com/maps/documentation/tile/3d-tiles-overview) API.",
        },
    ]
)


def build():
    # failure is tolerated.
    README.build(
        path=os.path.join(abcli_path_git, "google-earth-as-gltf/"),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
        help_function=lambda tokens: get_help(
            tokens,
            help_functions,
            mono=True,
        ),
    )

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
                "cols": 2,
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
            {
                "path": "google_earth",
            },
            {
                "path": "google_maps/api",
            },
            {
                "path": "google_maps/semseg/docs",
            },
        ]
        + [
            {
                "path": f"google_maps/semseg/docs/round-{index}.md",
            }
            for index in [1, 2, 3, 4, 5, 6]
        ]
    )
