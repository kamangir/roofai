#! /usr/bin/env bash

function test_roboflow_status() {
    local options=$1

    abcli_eval ,$options \
        roofai_roboflow_status \
        ,$options
}
