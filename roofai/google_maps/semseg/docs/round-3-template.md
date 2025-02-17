# Google Maps + SemSeg - round 3

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

```bash
runme() {
    local object_name=roof-dataset-one-1-$(@@timestamp)

    @roboflow download \
        project=roof-dataset-one,version=1,upload \
        $object_name

    @publish tar $object_name

    @assets publish \
        extensions=png,push \
        $object_name \
        --prefix _review/
}

runme
```

| | |
|-|-|
| assets:::roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/image.png | assets:::roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/mask.png |

set:::dataset_2 roof-dataset-one-1-2025-02-16-k7xo1q

object:::get:::dataset_2

details:::metadata
yaml:::get:::dataset_2
details:::

assets:::get:::dataset_2/00001-00000_png-rf-60c50dfd3edfe4472d69cb6b4c83b890.png

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)