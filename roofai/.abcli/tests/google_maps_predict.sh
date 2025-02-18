#! /usr/bin/env bash

function test_roofai_google_maps_predict() {
    local options=$1

    local prediction_object_name=test_roofai_google_maps_ingest_dataset-$(abcli_string_timestamp_short)

    abcli_eval ,$options \
        roofai_google_maps_get_predict \
        lat=$ROOFAI_TEST_GOOGLE_MAPS_HOUSE_LAT,lon=$ROOFAI_TEST_GOOGLE_MAPS_HOUSE_LON \
        profile=FULL \
        $ROOFAI_DEFAULT_GOOGLE_MAPS_MODEL \
        $prediction_object_name
}
