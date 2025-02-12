from blue_objects.README import Items


list_of_datasets = {
    "AIRS": {
        "description": "Aerial Imagery for Roof Segmentation from [kaggle](https://www.kaggle.com/datasets/atilol/aerialimageryforroofsegmentation).",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/roofAI/AIRS-cache-v45--review-index-2.png?raw=true",
    },
    "CamVid": {
        "description": "From [SegNet-Tutorial](https://github.com/alexgkendall/SegNet-Tutorial)",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/roofAI/0001TP_008850.png?raw=true",
    },
}


items = Items(
    [
        {
            "name": dataset_name,
            "url": f"./ingest/{dataset_name}.md",
            "marquee": details["thumbnail"],
            "description": details["description"],
        }
        for dataset_name, details in list_of_datasets.items()
    ]
)
