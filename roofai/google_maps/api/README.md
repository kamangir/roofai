# Google Maps API

## Maps Static

https://developers.google.com/maps/documentation/maps-static/start

```bash
runme(){
    local object_name=static-image-api-$(@@timestamp)

    local zoom
    for zoom in {1..19}; do
        @gmaps get_static_image - \
            $object_name \
            --lat $ROOFAI_TEST_GOOGLE_MAPS_LAT \
            --lon $ROOFAI_TEST_GOOGLE_MAPS_LON \
            --filename $(printf "%03d.png" $zoom) \
            --zoom $zoom
    done

    local scale
    for scale in 1 2 4; do
        @gif ~download,~upload \
            $object_name \
            --frame_duration 1000 \
            --scale $scale
    done

    @upload - $object_name

    @assets publish \
        extensions=gif+png,push \
        $object_name
}

runme
```

![image](https://github.com/kamangir/assets/blob/main/static-image-api-2025-02-15-wnfsd9/static-image-api-2025-02-15-wnfsd9-2X.gif?raw=true)

## Geocoding

https://developers.google.com/maps/documentation/geocoding/start

```python
from roofai.google_maps.api.geocoding import geocode

success, lat, lon, metadata = geocode(address="Vancouver Art Gallery", verbose=True)
assert success
```

> 🏛️  roofai.roofai.google_maps.api.geocoding.geocode(Vancouver Art Gallery): lat:49.282961, lon:-123.120471
