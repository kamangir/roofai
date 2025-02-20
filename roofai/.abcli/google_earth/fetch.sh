#! /usr/bin/env bash

function roofai_google_earth_fetch() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 0)
    local lat=$(abcli_option "$options" lat 0)
    local lon=$(abcli_option "$options" lon 0)

    local object_name=$(abcli_clarify_object $2 fetch-$lat-$lon-$(abcli_string_timestamp_short))

    local path=$(python3 -m roofai locate)/google_earth/gltf/
    abcli_eval dryrun=$do_dryrun,path=$path \
        node fetch-tiles.js \
        $lat \
        $lon \
        $object_name \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}
