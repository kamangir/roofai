# Google Maps + SemSeg

## ingesting a dataset and uploading it to roboflow for labelling

```bash
roofai dataset ingest \
    source=gmaps,upload - \
    count=100,lat=53.343318,lon=-2.650661 \
    roboflow,create,project=roof-dataset-two
```

https://app.roboflow.com/kamangir/roof-dataset-two/annotate


set:::gmaps_dataset gmaps-dataset-2025-02-16-7b2zxk

details:::metadata
yaml:::get:::gmaps_dataset:::roofai-roofai-google_maps-semseg-dataset
details:::

assets:::roofAI/roboflow/labelling-2.png

## downloading the labelled dataset from roboflow

```bash
@roboflow download \
    project=roof-dataset-two,version=5,upload - \
    ingest,count=10000,upload -
```

set:::object_name_1 roof-dataset-one-1-2025-02-16-k7xo1q
set:::dataset_object_name_1 roof-dataset-two-5-2025-02-16-mvhttg-ingest-2025-02-17-0yqil7

| | |
|-|-|
| assets:::roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/image.png | assets:::roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/mask.png |
| assets:::get:::object_name_1/00001-00000_png-rf-60c50dfd3edfe4472d69cb6b4c83b890.png  | assets:::get:::dataset_object_name_1/00003-00000_png-rf-005aa82fabd5523b81afa254257e976f-00000-00000.png |

---

set:::object_name_3 roof-dataset-two-5-2025-02-17-u3s0js

object:::get:::object_name_3

details:::metadata
yaml:::get:::object_name_3
details:::

set:::dataset_object_name_2 roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau

object:::get:::dataset_object_name_2

details:::metadata
yaml:::get:::dataset_object_name_2
details:::

## training a model

```bash
roofai semseg train \
    profile=FULL,upload \
    roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau - \
    --classes roof \
    --epoch_count 5
```

set:::model_object_name roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau-model-2025-02-17-tj4kih

object:::get:::model_object_name

| | |
|-|-|
| assets:::get:::model_object_name/train-summary.png | assets:::get:::model_object_name/predict-00000.png |

## prediction

```bash
runme() {
    local prediction_object_name=prediction-$(@@timestamp)

    @gmaps predict \
        lat=$ROOFAI_TEST_GOOGLE_MAPS_HOUSE_LAT,lon=$ROOFAI_TEST_GOOGLE_MAPS_HOUSE_LON \
        profile=FULL,upload - \
        $prediction_object_name

    @publish tar $prediction_object_name

    @assets publish \
        extensions=png,push \
        $prediction_object_name
}

runme
```

set:::prediction_object_name prediction-2025-02-17-1tuy6j

object:::get:::prediction_object_name

| | |
|-|-|
| assets:::get:::prediction_object_name/input.png | assets:::get:::prediction_object_name/prediction.png |

details:::metadata
yaml:::get:::dataset_object_name_2
details:::

🔥

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)
- [round 3](./round-3.md)
- [round 4](./round-4.md)
- [round 5](./round-5.md)
- [round 6](./round-6.md)