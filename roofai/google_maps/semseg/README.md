# Google Maps + SemSeg

## ingesting a dataset and uploading it to [roboflow](https://docs.roboflow.com/)

🔥

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


[gmaps-dataset-2025-02-15-ueo77u](https://kamangir-public.s3.ca-central-1.amazonaws.com/gmaps-dataset-2025-02-15-ueo77u.tar.gz)


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
count: 10
grid:
- 3
- 4
lat: 53.343318
lon: -2.650661
maptype: satellite
size: 640x640
zoom: 20

```

</details>


