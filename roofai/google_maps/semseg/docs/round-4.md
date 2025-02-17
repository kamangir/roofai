# Google Maps + SemSeg - round 4

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


[roof-dataset-two-5-2025-02-16-mvhttg-ingest-2025-02-17-0yqil7](https://kamangir-public.s3.ca-central-1.amazonaws.com/roof-dataset-two-5-2025-02-16-mvhttg-ingest-2025-02-17-0yqil7.tar.gz)


<details>
<summary>metadata</summary>

```yaml
bucket: kamangir
channel: {}
classes:
- background
- roof
ingested-by: roofai.roofai.dataset.ingest.from_dataset-6.179.1
kind: CamVid
num:
  test: 19
  train: 156
  val: 19
prefix: bolt/roof-dataset-two-5-2025-02-16-mvhttg-ingest-2025-02-17-0yqil7
source: roof-dataset-two-5-2025-02-16-mvhttg

```

</details>


![image](https://github.com/kamangir/assets/blob/main/roof-dataset-two-5-2025-02-16-mvhttg-ingest-2025-02-17-0yqil7/00003-00000_png-rf-005aa82fabd5523b81afa254257e976f-00000-00000.png?raw=true)

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)
- [round 3](./round-3.md)
