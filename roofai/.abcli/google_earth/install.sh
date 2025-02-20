#! /usr/bin/env bash

function abcli_install_roofai_google_earth() {

    abcli_git_clone https://github.com/OmarShehata/google-earth-as-gltf.git

    local path=$(python3 -m roofai locate)/google_earth/gltf/
    abcli_eval path=$path \
        npm install
}

abcli_install_module roofai_google_earth 1.1.1
