#! /usr/bin/env bash

function roofai_google_maps_ingest_dataset() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    local object_name=$(abcli_clarify_object $2 gmaps-dataset-$(abcli_string_timestamp_short))
    local object_path=$ABCLI_OBJECT_ROOT/$object_name

    local ingest_options=$3
    local lat=$(abcli_option "$ingest_options" lat 0)
    local lon=$(abcli_option "$ingest_options" lon 0)
    local count=$(abcli_option "$ingest_options" count 10)

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofai.google_maps \
        ingest_dataset \
        --lat $lat \
        --lon $lon \
        --count $count \
        --object_name $object_name \
        "${@:4}"
    local status="$?"

    [[ "$do_dryrun" == 0 ]] &&
        abcli_cat $object_path/metadata.yaml

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
