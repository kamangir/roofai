#! /usr/bin/env bash

function test_roofai_version() {
    local options=$1

    abcli_eval ,$options \
        "roofai version ${@:2}"
}
