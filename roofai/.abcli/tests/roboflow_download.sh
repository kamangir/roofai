#! /usr/bin/env bash

function test_roofai_roboflow_download() {
    local options=$1

    local object_name=test_roofai_roboflow_download-$(abcli_string_timestamp_short)
    local dataset_object_name=$object_name-ingest-$(abcli_string_timestamp_short)

    abcli_eval ,$options \
        roofai_roboflow_download \
        project=roof-dataset-one,version=1 \
        $object_name \
        ingest,count=10000 \
        $dataset_object_name
}
