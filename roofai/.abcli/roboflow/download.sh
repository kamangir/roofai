#! /usr/bin/env bash

function roofai_roboflow_download() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 0)
    local do_clean=$(abcli_option_int "$options" clean 1)
    local do_review=$(abcli_option_int "$options" review 1)
    local project_name=$(abcli_option "$options" project roofai-generic)
    local version=$(abcli_option "$options" version 1)

    local object_name=$(abcli_clarify_object $2 $project_name-$version-$(abcli_string_timestamp_short))

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.roboflow \
        download \
        --clean $do_clean \
        --project_name $project_name \
        --version $version \
        --object_name $object_name \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    if [[ "$do_review" == 1 ]]; then
        roofai_dataset_review - \
            $object_name \
            --subset train \
            --index 0
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name
}
