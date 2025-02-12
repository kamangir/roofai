# Static Image API

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

    @gif ~download $object_name \
        --frame_duration 1000

    @upload - $object_name

    @assets publish \
        extension=gif,push \
	    $object_name
}

runme
```

set:::object_name static-image-api-2025-02-11-an1gvf

assets:::get:::object_name/get:::object_name.gif