#! /usr/bin/env bash

function test_roofai_google_maps_ingest_dataset() {
    local options=$1

    local object_name=test_roofai_google_maps_ingest_dataset-$(abcli_string_timestamp_short)

    abcli_eval ,$options \
        roofai_dataset_ingest \
        source=gmaps \
        $object_name \
        count=3,lat=53.343318,lon=-2.650661,zoom=20 \
        roboflow,project=roofai-bash-test-roboflow-create-project
}
