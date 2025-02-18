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
    project=roof-dataset-two,version=5,upload - \
    ingest,count=10000,upload -
```


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/image.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/mask.png?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/roof-dataset-one-1-2025-02-16-k7xo1q/00001-00000_png-rf-60c50dfd3edfe4472d69cb6b4c83b890.png?raw=true)  | ![image](https://github.com/kamangir/assets/blob/main/roof-dataset-two-5-2025-02-16-mvhttg-ingest-2025-02-17-0yqil7/00003-00000_png-rf-005aa82fabd5523b81afa254257e976f-00000-00000.png?raw=true) |

---


[roof-dataset-two-5-2025-02-17-u3s0js](https://kamangir-public.s3.ca-central-1.amazonaws.com/roof-dataset-two-5-2025-02-17-u3s0js.tar.gz)


<details>
<summary>metadata</summary>

```yaml
classes:
- background
- roof
ingested-by: roofai-6.190.1
kind: CamVid
roofai-roofai-roboflow-download:
  input:
    project: roof-dataset-two
    version: 5
source: gmaps

```

</details>



[roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau](https://kamangir-public.s3.ca-central-1.amazonaws.com/roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau.tar.gz)


<details>
<summary>metadata</summary>

```yaml
bucket: kamangir
channel: {}
classes:
- background
- roof
ingested-by: roofai.roofai.dataset.ingest.from_dataset-6.190.1
kind: CamVid
num:
  test: 19
  train: 156
  val: 19
prefix: bolt/roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau
source: roof-dataset-two-5-2025-02-17-u3s0js

```

</details>


## training a model

```bash
roofai semseg train \
    profile=FULL,upload \
    roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau - \
    --classes roof \
    --epoch_count 5
```


[roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau-model-2025-02-17-tj4kih](https://kamangir-public.s3.ca-central-1.amazonaws.com/roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau-model-2025-02-17-tj4kih.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau-model-2025-02-17-tj4kih/train-summary.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau-model-2025-02-17-tj4kih/predict-00000.png?raw=true) |

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


[prediction-2025-02-18-u0frtv](https://kamangir-public.s3.ca-central-1.amazonaws.com/prediction-2025-02-18-u0frtv.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/prediction-2025-02-18-u0frtv/input.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/prediction-2025-02-18-u0frtv/prediction.png?raw=true) |


<details>
<summary>metadata</summary>

```yaml
roofai-roofai-google_maps-semseg-predict:
  address: ''
  elapsed_time: 1.5131659507751465
  lat: 53.343318
  lon: -2.650661
  model: roof-dataset-two-5-2025-02-17-u3s0js-ingest-2025-02-17-rohoau-model-2025-02-17-tj4kih
  output_filename: prediction.png

```

</details>


🔥

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)
- [round 3](./round-3.md)
- [round 4](./round-4.md)
- [round 5](./round-5.md)
- [round 6](./round-6.md)
