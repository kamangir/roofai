#! /usr/bin/env bash

function test_google_maps_geocode() {
    local options=$1

    local object_name=test_google_maps_geocode-$(abcli_string_timestamp_short)

    roofai_google_maps_geocode \
        - \
        $object_name \
        --address "350 W Georgia St, Vancouver, BC V6B 6B1, Canada" \
        --verbose 1
}
