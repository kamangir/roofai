#! /usr/bin/env bash

function roofai_google_maps_get_static_image() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $2 $(abcli_string_timestamp_short))

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.google_maps \
        get_static_image \
        --object_name $object_name \
        "${@:3}"
}
