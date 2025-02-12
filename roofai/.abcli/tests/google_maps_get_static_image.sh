#! /usr/bin/env bash

function test_google_maps_get_static_image() {
    local options=$1

    local object_name=test_google_maps_get_static_image-$(abcli_string_timestamp_short)

    roofai_google_maps_get_static_image \
        - \
        $object_name \
        --lat $ROOFAI_TEST_GOOGLE_MAPS_LAT \
        --lon $ROOFAI_TEST_GOOGLE_MAPS_LON \
        --filename $(@@timestamp).png \
        --zoom 19
}
