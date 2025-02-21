#! /usr/bin/env bash

function roofai_google_earth_browse() {
    local options=$1
    local do_dev=$(abcli_option_int "$options" dev 0)
    local do_sandbox=$(abcli_option_int "$options" sandbox 0)

    local url
    if [[ "$do_sandbox" == 1 ]]; then
        url=https://sandbox.babylonjs.com/
    elif [[ "$do_dev" == 1 ]]; then
        [[ "$abcli_is_github_workflow" == true ]] &&
            return 0

        pushd $abcli_path_git/google-earth-as-gltf >/dev/null
        npm install

        abcli_browse http://localhost:3000/ &
        npm run dev
        popd >/dev/null
    else
        url=https://kamangir.github.io/google-earth-as-gltf/
    fi

    abcli_browse $url
}
