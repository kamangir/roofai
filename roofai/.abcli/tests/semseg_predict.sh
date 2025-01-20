#! /usr/bin/env bash

function test_roofai_semseg_predict() {
    local options=$1

    local prediction_object_name=test_roofai_semseg_predict-$(abcli_string_timestamp_short)

    abcli_eval ,$options \
        roofai_semseg_predict \
        profile=VALIDATION,$4 \
        $TEST_roofAI_semseg_model_AIRS_full_v1 \
        $TEST_roofAI_ingest_AIRS_v2 \
        $prediction_object_name \
        "${@:5}"
}
