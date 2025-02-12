#! /usr/bin/env bash

function roofai_google_maps() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=roofai_google_maps_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m roofai.google_maps "$@"
}

abcli_source_caller_suffix_path /google_maps
