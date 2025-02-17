#! /usr/bin/env bash

function roofai_roboflow_create_project() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local project_name=$(abcli_option "$options" project roofai-generic)

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.roboflow \
        create_project \
        --project_name $project_name \
        "${@:2}"
}
