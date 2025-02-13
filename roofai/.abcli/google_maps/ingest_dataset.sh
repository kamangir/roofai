#! /usr/bin/env bash

function roofai_google_maps_ingest_dataset() {
    local options=$1

    local object_name=$(abcli_clarify_object $2 gmaps-dataset-$(abcli_string_timestamp_short))

    :
}
