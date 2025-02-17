# Google Maps + SemSeg

> purpose: ingesting a dataset and uploading it to roboflow for labelling, and then training a model.

```bash
roofai dataset ingest \
    source=gmaps,upload - \
    count=100,lat=53.343318,lon=-2.650661 \
    roboflow,create,project=roof-dataset-two
```

https://app.roboflow.com/kamangir/roof-dataset-two/annotate


set:::object_name gmaps-dataset-2025-02-16-7b2zxk

details:::metadata
yaml:::get:::object_name:::roofai-roofai-google_maps-semseg-dataset
details:::

assets:::roofAI/roboflow/labelling-2.png

⚠️ low quality of the model.

---

- [round 1](./round-1.md)