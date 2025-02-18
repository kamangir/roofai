#! /usr/bin/env bash

function roofai_google_maps_predict() {
    local options=$1
    local lat=$(abcli_option "$options" lat 0)
    local lon=$(abcli_option "$options" lon 0)

    local predict_options=$2
    $abcli_gpu_status_cache && local device=cuda || local device=cpu
    local device=$(abcli_option "$predict_options" device $device)
    local do_dryrun=$(abcli_option_int "$predict_options" dryrun 0)
    local do_download=$(abcli_option_int "$predict_options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$predict_options" upload 0)
    local profile=$(abcli_option "$predict_options" profile VALIDATION)

    local model_object_name=$(abcli_clarify_object $3 $ROOFAI_DEFAULT_GOOGLE_MAPS_MODEL)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $model_object_name

    local prediction_object_name="prediction-$lat-$lon-$(abcli_string_timestamp_short)"
    prediction_object_name=$(echo $prediction_object_name | tr . -)
    prediction_object_name=$(abcli_clarify_object $4 $prediction_object_name)

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.google_maps \
        predict \
        --lat $lat \
        --lon $lon \
        --device $device \
        --model_object_name $model_object_name \
        --profile $profile \
        --prediction_object_name $prediction_object_name \
        "${@:5}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $prediction_object_name

    return 0
}
