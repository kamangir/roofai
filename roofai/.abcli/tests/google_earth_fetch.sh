#! /usr/bin/env bash

function test_roofai_google_earth_fetch() {
    local options=$1

    local object_name=test_roofai_google_earth_fetch-$(abcli_string_timestamp_short)

    abcli_eval ,$options \
        roofai_google_earth_fetch \
        lat=$ROOFAI_TEST_GOOGLE_MAPS_HOUSE_LAT,lon=$ROOFAI_TEST_GOOGLE_MAPS_HOUSE_LON \
        $object_name
}
