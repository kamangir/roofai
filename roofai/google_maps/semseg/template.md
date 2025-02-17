# Google Maps + SemSeg

## ingesting a dataset

```bash
runme() {
    local object_name=gmaps-dataset-$(@@timestamp)

    roofai dataset ingest \
        source=gmaps,upload \
        $object_name \
        count=10,lat=53.343318,lon=-2.650661,zoom=20

    @publish ~download,tar $object_name
}

runme
```

set:::object_name gmaps-dataset-2025-02-15-ueo77u

object:::get:::object_name

details:::metadata
yaml:::get:::object_name:::roofai-roofai-google_maps-semseg-dataset
details:::

## ingesting a dataset and uploading it to roboflow for labelling

```bash
roofai dataset ingest \
    source=gmaps - \
    count=10,lat=53.343318,lon=-2.650661 \
    roboflow,create,project=roof-dataset-one
```

https://app.roboflow.com/kamangir/roof-dataset-one/annotate


assets:::roofAI/roboflow/labelling-2.png


🔥