#! /usr/bin/env bash

function roofai_roboflow_upload() {
    local options=$1
    local do_create=$(abcli_option_int "$options" create 1)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local project_name=$(abcli_option "$options" project roofai-generic)

    local object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.roboflow \
        upload \
        --object_name "$object_name" \
        --create $do_create \
        --project_name $project_name \
        "${@:3}"
}
