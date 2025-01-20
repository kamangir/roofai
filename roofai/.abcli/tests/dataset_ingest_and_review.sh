#! /usr/bin/env bash

function test_roofai_dataset_ingest_and_review() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local list_of_sources="CamVid+palisades-dataset-v1"
    [[ "$abcli_is_github_workflow" == false ]] &&
        list_of_sources="AIRS+$list_of_sources"
    list_of_sources=$(abcli_option "$options" source $list_of_sources)

    local source
    for source in $(echo $list_of_sources | tr + " "); do
        abcli_log "📜 ingesting $source..."

        local dataset_object_name=test_roofai_dataset_ingest_and_review-$source-$(abcli_string_timestamp_short)

        abcli_eval dryrun=$do_dryrun \
            roofai_dataset_ingest \
            source=$source,$2 \
            $dataset_object_name \
            --test_count 16 \
            --train_count 16 \
            --val_count 16
        [[ $? -ne 0 ]] && return 1

        abcli_eval dryrun=$do_dryrun \
            roofai_dataset_review \
            ,$3 \
            $dataset_object_name \
            --index 1 \
            --subset train \
            "${@:4}"
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done
}
