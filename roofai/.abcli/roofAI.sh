#! /usr/bin/env bash

export NO_ALBUMENTATIONS_UPDATE=1

function roofai() {
    local task=$(abcli_unpack_keyword $1 version)

    abcli_generic_task \
        plugin=roofai,task=$task \
        "${@:2}"
}

abcli_log $(roofai version --show_icon 1)
