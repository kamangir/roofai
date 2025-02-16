#! /usr/bin/env bash

function test_roofai_README() {
    local options=$1

    abcli_eval ,$options \
        roofai build_README
}
