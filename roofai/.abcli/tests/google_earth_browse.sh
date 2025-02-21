#! /usr/bin/env bash

function test_roofai_google_earth_browse() {
    local options=$1

    local test_options
    for test_options in "" dev sandbox; do
        roofai_google_earth_browse $options,$test_options
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
