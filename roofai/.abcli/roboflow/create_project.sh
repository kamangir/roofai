#! /usr/bin/env bash

function roofai_roboflow_create_project() {
    local options=$1

    python3 -m roofai.roboflow \
        create_project \
        "${@:2}"
}
