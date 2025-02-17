#! /usr/bin/env bash

function test_roofai_roboflow_create_project() {
    local options=$1

    abcli_eval ,$options \
        roofai_roboflow_create_project \
        project=roofai-bash-test-roboflow-create-project,$options \
        --description "created-by-bashtest"
}
