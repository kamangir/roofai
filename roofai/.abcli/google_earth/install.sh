#! /usr/bin/env bash

export ROOFAI_PATH_GLTF=$abcli_path_git/google-earth-as-gltf/simple-node-example/

function abcli_install_roofai_google_earth() {
    abcli_git_clone https://github.com/kamangir/google-earth-as-gltf.git

    abcli_eval path=$ROOFAI_PATH_GLTF \
        npm install
}

abcli_install_module roofai_google_earth 1.6.1
