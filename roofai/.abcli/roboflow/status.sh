#! /usr/bin/env bash

function roofai_roboflow_status() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.roboflow \
        get_status \
        "${@:2}"
}
