#! /usr/bin/env bash

function test_roofai_semseg_train() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local source=$(abcli_option "$options" source AIRS)

    local dataset_object_name=$TEST_roofAI_ingest_AIRS_v1

    abcli_log "📜 training on $source - dataset: $dataset_object_name"

    local classes=car
    [[ "$source" == AIRS ]] && local classes=roof

    local model_object_name=test_roofai_semseg_train_and_predict-model-$(abcli_string_timestamp_short)

    abcli_eval dryrun=$do_dryrun \
        roofai_semseg_train \
        profile=VALIDATION,~upload,$3 \
        $dataset_object_name \
        $model_object_name \
        --classes $classes
}
