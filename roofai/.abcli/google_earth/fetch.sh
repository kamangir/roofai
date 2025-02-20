#! /usr/bin/env bash

function roofai_google_earth_fetch() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_install=$(abcli_option_int "$options" install 0)
    local do_upload=$(abcli_option_int "$options" upload 0)
    local lat=$(abcli_option "$options" lat 0)
    local lon=$(abcli_option "$options" lon 0)

    local object_name=$(abcli_clarify_object $2 fetch-$lat-$lon-$(abcli_string_timestamp_short))

    if [[ "$do_install" ]]; then
        abcli_eval dryrun=$do_dryrun,path=$ROOFAI_PATH_GLTF \
            npm install
        [[ $? -ne 0 ]] && return 1
    fi

    abcli_eval dryrun=$do_dryrun,path=$ROOFAI_PATH_GLTF \
        node fetch-tiles.js \
        $lat \
        $lon \
        $ABCLI_OBJECT_ROOT/$object_name \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}
