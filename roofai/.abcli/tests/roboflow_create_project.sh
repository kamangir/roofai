#! /usr/bin/env bash

function test_roboflow_create_project() {
    local options=$1

    abcli_eval ,$options \
        roofai_roboflow_create_project \
        ,$options \
        --name test-$(abcli_string_timestamp_short) \
        --description "created-by-bashtest"
}
