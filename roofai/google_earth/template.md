# Photorealistic 3D Tiles

- API: https://developers.google.com/maps/documentation/tile/3d-tiles-overview
- 3D Area Explorer: https://js-3d-area-explorer-demo-dev-t6a6o7lkja-uc.a.run.app/#location.coordinates.lat=53.4044838&location.coordinates.lng=-2.6585317


```bash
runme() {
    local object_name=fetch-$(@@timestamp)

    @gearth fetch \
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

set:::object_name fetch-2025-02-20-oeqz75

| | | |
|-|-|-|
| assets:::get:::object_name/google-earth-as-gltf.png | assets:::get:::object_name/babylonjs.png | assets:::get:::object_name/notebook.png |
| using [google-earth-as-gltf](https://github.com/kamangir/google-earth-as-gltf/tree/main/simple-node-example) [[live](https://kamangir.github.io/google-earth-as-gltf/)] | glb viewer: [sandbox.babylonjs.com](https://sandbox.babylonjs.com/) | [notebook](../../notebooks/google_earth.ipynb) wip |

assets:::get:::object_name/

object:::get:::object_name