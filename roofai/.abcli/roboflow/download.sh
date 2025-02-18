#! /usr/bin/env bash

function roofai_roboflow_download() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 0)
    local do_clean=$(abcli_option_int "$options" clean 1)
    local do_review=$(abcli_option_int "$options" review 1)
    local project_name=$(abcli_option "$options" project roofai-generic)
    local version=$(abcli_option "$options" version 1)

    local zoom=$(abcli_mlflow_tags_get \
        $project_name \
        --tag zoom)
    abcli_log "zoom: $zoom"

    local object_name=$(abcli_clarify_object $2 $project_name-$version-$(abcli_string_timestamp_short))

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.roboflow \
        download \
        --clean $do_clean \
        --project_name $project_name \
        --version $version \
        --object_name $object_name
    [[ $? -ne 0 ]] && return 1

    abcli_mlflow_tags_set \
        $object_name \
        zoom=$zoom

    if [[ "$do_review" == 1 ]]; then
        roofai_dataset_review - \
            $object_name \
            --subset train \
            --index 0
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    local ingest_options=$3
    local do_ingest=$(abcli_option_int "$ingest_options" ingest 0)
    [[ "$do_ingest" == 0 ]] &&
        return 0

    local count=$(abcli_option "$ingest_options" count 1000)

    local dataset_object_name=$(abcli_clarify_object $4 $object_name-ingest-$(abcli_string_timestamp_short))

    abcli_mlflow_tags_set \
        $dataset_object_name \
        zoom=$zoom

    roofai_dataset_ingest \
        ~download,source=$object_name,$ingest_options \
        $dataset_object_name \
        --test_count $(python3 -c "print(int($count*0.1))") \
        --train_count $(python3 -c "print(int($count*0.8))") \
        --val_count $(python3 -c "print(int($count*0.1))")
}
