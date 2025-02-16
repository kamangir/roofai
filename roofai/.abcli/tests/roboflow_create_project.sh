#! /usr/bin/env bash

function test_roboflow_create_project() {
    local options=$1

    abcli_eval ,$options \
        roofai_roboflow_create_project \
        ,$options \
        --name roofai-bash-test-roboflow-create-project \
        --description "created-by-bashtest"
}
