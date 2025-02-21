# Photorealistic 3D Tiles

- API: https://developers.google.com/maps/documentation/tile/3d-tiles-overview
- 3D Area Explorer: https://js-3d-area-explorer-demo-dev-t6a6o7lkja-uc.a.run.app/#location.coordinates.lat=53.4044838&location.coordinates.lng=-2.6585317


```bash
runme() {
    local object_name=fetch-$(@@timestamp)

    @google_earth fetch \
        install,upload \
        $object_name \
        --latitude=$ROOFAI_TEST_GOOGLE_MAPS_LAT \
        --longitude=$ROOFAI_TEST_GOOGLE_MAPS_LON \
        --zoom=16
    
    @publish tar $object_name

    @assets publish \
        extensions=png,push \
        $object_name
}

runme
```


| | | |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/fetch-2025-02-20-oeqz75/google-earth-as-gltf.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/fetch-2025-02-20-oeqz75/babylonjs.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/fetch-2025-02-20-oeqz75/notebook.png?raw=true) |
| using [google-earth-as-gltf](https://github.com/kamangir/google-earth-as-gltf/tree/main/simple-node-example) [[live](https://kamangir.github.io/google-earth-as-gltf/)] | glb viewer: [sandbox.babylonjs.com](https://sandbox.babylonjs.com/) | [notebook](../../notebooks/google_earth.ipynb) wip |

[](https://github.com/kamangir/assets/blob/main/fetch-2025-02-20-oeqz75/)

[fetch-2025-02-20-oeqz75](https://kamangir-public.s3.ca-central-1.amazonaws.com/fetch-2025-02-20-oeqz75.tar.gz)
