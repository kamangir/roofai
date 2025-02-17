# Google Maps + SemSeg

## ingesting a dataset and uploading it to roboflow for labelling

```bash
roofai dataset ingest \
    source=gmaps,upload - \
    count=100,lat=53.343318,lon=-2.650661 \
    roboflow,create,project=roof-dataset-two
```

https://app.roboflow.com/kamangir/roof-dataset-two/annotate




<details>
<summary>metadata</summary>

```yaml
center:
  gsd: 0.08912957603498574
  size:
    deg:
    - 0.0005124253466836525
    - 0.0008583068847215374
    m:
    - 57.04292866239087
    - 57.04292866239087
    px:
    - 640
    - 640
count: 100
grid:
- 10
- 10
lat: 53.343318
lon: -2.650661
maptype: satellite
size: 640x640
zoom: 20

```

</details>


![image](https://github.com/kamangir/assets/blob/main/roofAI/roboflow/labelling-2.png?raw=true)

## downloading the labelled dataset from roboflow

```bash
@roboflow download \
    project=roof-dataset-two,version=5,upload -
```

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/image.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/mask.png?raw=true) |


![image](https://github.com/kamangir/assets/blob/main/roof-dataset-one-1-2025-02-16-k7xo1q/00001-00000_png-rf-60c50dfd3edfe4472d69cb6b4c83b890.png?raw=true)

---


[roof-dataset-two-5-2025-02-16-mvhttg](https://kamangir-public.s3.ca-central-1.amazonaws.com/roof-dataset-two-5-2025-02-16-mvhttg.tar.gz)


<details>
<summary>metadata</summary>

```yaml
classes:
- background
- roof
ingested-by: roofai-6.174.1
kind: CamVid
roofai-roofai-roboflow-download:
  input:
    project: roof-dataset-two
    version: 5
source: gmaps

```

</details>


🔥

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)
- [round 3](./round-3.md)
