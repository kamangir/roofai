#! /usr/bin/env bash

function roofai_google_maps_geocode() {
    local options=$1

    local object_name=$(abcli_clarify_object $2 $(abcli_string_timestamp_short))

    python3 -m roofai.google_maps \
        geocode \
        --object_name $object_name \
        "${@:3}"
}
