# Google Maps + SemSeg

## ingesting a dataset and uploading it to roboflow for labelling

```bash
roofai dataset ingest \
    source=gmaps,upload - \
    count=100,lat=53.343318,lon=-2.650661 \
    roboflow,create,project=roof-dataset-two
```

https://app.roboflow.com/kamangir/roof-dataset-two/annotate


set:::dataset_1 gmaps-dataset-2025-02-16-7b2zxk

details:::metadata
yaml:::get:::dataset_1:::roofai-roofai-google_maps-semseg-dataset
details:::

assets:::roofAI/roboflow/labelling-2.png

## downloading the labelled dataset from roboflow

🔥

```bash
@roboflow download \
    project=roof-dataset-two,version=5,~upload - \
    ingest,count=10000,~upload -
```

TODO: ~upload -> upload

🔥

| | |
|-|-|
| assets:::roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/image.png | assets:::roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/mask.png |

set:::dataset_2 roof-dataset-one-1-2025-02-16-k7xo1q

assets:::get:::dataset_2/00001-00000_png-rf-60c50dfd3edfe4472d69cb6b4c83b890.png

---

set:::dataset_3 roof-dataset-two-5-2025-02-16-mvhttg

object:::get:::dataset_3

details:::metadata
yaml:::get:::dataset_3
details:::

```bash
runme() {
    local dataset_object_name=roof-dataset-two-5-2025-02-16-mvhttg
    local object_name=$dataset_object_name-ingest-$(@@timestamp)

    roofai dataset ingest \
        source=$dataset_object_name,upload \
        $object_name \
        --test_count 1000 \
        --train_count 8000 \
        --val_count 1000

    @publish tar $object_name

    @assets publish \
        extensions=png,push \
        $object_name \
        --prefix _review/
}

runme
```

set:::dataset_4 roof-dataset-two-5-2025-02-16-mvhttg-ingest-2025-02-17-0yqil7

object:::get:::dataset_4

details:::metadata
yaml:::get:::dataset_4
details:::

assets:::get:::dataset_4/00003-00000_png-rf-005aa82fabd5523b81afa254257e976f-00000-00000.png

🔥

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)
- [round 3](./round-3.md)
- [round 4](./round-4.md)