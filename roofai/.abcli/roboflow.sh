#! /usr/bin/env bash

function roofai_roboflow() {
    local task=$(abcli_unpack_keyword $1 void)

    local function_name=roofai_roboflow_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m roofai.roboflow "$@"
}

abcli_source_caller_suffix_path /roboflow
