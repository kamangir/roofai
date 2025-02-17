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

🔥

```bash
@roboflow download \
	project=roof-dataset-one,version=1 -
```

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/image.png?raw=true) | assets::roofAI/roboflow/roof-dataset-one-1-2025-02-16-k9ezfk/mask.png |

🚧

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)
