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

    local zoom=$(abcli_mlflow_tags_get \
        $object_name \
        --tag zoom)
    abcli_log "zoom: $zoom"
    abcli_mlflow_tags_set \
        $project_name \
        zoom=$zoom

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.roboflow \
        upload \
        --create $do_create \
        --project_name $project_name \
        --object_name $object_name \
        "${@:3}"
}
