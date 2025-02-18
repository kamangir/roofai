# 🏛️ roofai

everything AI about roofs. 🏛️

```bash
pip install roofai
```

```mermaid
graph LR
    dataset_ingest["roofai<br>dataset<br>ingest<br>source=AIRS|CamVid|&lt;distributed-dataset&gt;<br>&lt;dataset-object-name&gt;"]

    dataset_review["roofai<br>dataset<br>review -<br>&lt;dataset-object-name&gt;"]

    semseg_train["roofai<br>semseg<br>train -<br>&lt;dataset-object-name&gt;<br>&lt;model-object-name&gt;"]

    semseg_predict["roofai<br>semseg<br>predict -<br>&lt;model-object-name&gt;<br>&lt;dataset-object-name&gt;<br>&lt;prediction-object-name&gt;"]

    gmaps_get_static_image["@gmaps<br>get_static_image -<br>&lt;object-name&gt;<br>--lat &lt;lat&gt;<br>--lon &lt;lon&gt;"]

    gmaps_geocode["@gmaps<br>geocode - -<br>--address &lt;address&gt;"]

    dataset_ingest_gmaps["roofai<br>dataset<br>ingest<br>source=gmaps<br>&lt;object-name&gt;<br>count=&lt;count&gt;,lat=&lt;lat&gt;,lon=&lt;lon&gt;<br>roboflow,project=&lt;project-name&gt;"]

    roboflow_upload["@roboflow<br>upload<br>project=&lt;project-name&gt;<br>&lt;object-name&gt;"]

    roboflow_download["@roboflow<br>download<br>project=&lt;project-name&gt;,version=&lt;version&gt;<br>&lt;object-name&gt;<br>ingest,count=&lt;10000&gt;<br>&lt;dataset-object-name&gt;"]

    gmaps_predict["@gmaps<br>predict<br>lat=&lt;lat&gt;,lon=&lt;lon&gt; -<br>&lt;model-object-name&gt;<br>&lt;prediction-object-name&gt;"]

    address["🌐 address"]:::folder
    lat_lon["🌐 lat,lon"]:::folder
    AIRS["AIRS"]:::folder
    CamVid["CamVid"]:::folder
    dataset_object_name["📂 dataset object"]:::folder
    distributed_dataset_object_name["📂 distributed dataset object"]:::folder
    model_object_name["📂 model object"]:::folder
    prediction_object_name["📂 prediction object"]:::folder
    object_name["📂 object"]:::folder
    object_name_static_image["📂 object"]:::folder
    terminal["💻 terminal"]:::folder
    roboflow["🖼️ roboflow"]:::folder

    lat_lon --> gmaps_predict
    address --> gmaps_predict
    model_object_name --> gmaps_predict
    gmaps_predict --> prediction_object_name

    dataset_object_name --> dataset_ingest
    distributed_dataset_object_name --> dataset_ingest
    AIRS --> dataset_ingest
    CamVid --> dataset_ingest
    dataset_ingest --> dataset_object_name

    dataset_ingest_gmaps --> gmaps_get_static_image
    dataset_ingest_gmaps --> roboflow
    dataset_ingest_gmaps --> object_name

    object_name --> roboflow_upload
    roboflow_upload --> roboflow

    roboflow --> roboflow_download
    roboflow_download --> dataset_ingest
    roboflow_download --> dataset_review
    roboflow_download --> dataset_object_name

    AIRS --> dataset_review
    distributed_dataset_object_name --> dataset_review
    CamVid --> dataset_review
    dataset_object_name --> dataset_review
    dataset_review --> terminal

    dataset_object_name --> semseg_train
    semseg_train --> model_object_name

    model_object_name --> semseg_predict
    dataset_object_name --> semseg_predict
    semseg_predict --> prediction_object_name

    lat_lon --> gmaps_get_static_image
    gmaps_get_static_image --> object_name_static_image

    address --> gmaps_geocode
    gmaps_geocode --> lat_lon

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

|   |   |
| --- | --- |
| [`Datasets`](./roofai/dataset) [![image](https://github.com/kamangir/assets/blob/main/roofAI/AIRS-cache-v45--review-index-2.png?raw=true)](./roofai/dataset) Semantic Segmentation Datasets | [`Semantic Segmentation (SemSeg)`](./roofai/semseg) [![image](./assets/predict-00247.png)](./roofai/semseg) A Semantic Segmenter based on [segmentation_models.pytorch](<https://github.com/qubvel/segmentation_models.pytorch/blob/master/examples/cars%20segmentation%20(camvid).ipynb>). |
| [`Google Maps API`](./roofai/google_maps/api) [![image](https://github.com/kamangir/assets/blob/main/static-image-api-2025-02-15-wnfsd9/static-image-api-2025-02-15-wnfsd9-2X.gif?raw=true)](./roofai/google_maps/api) Integrations with the Google Maps [Static](https://developers.google.com/maps/documentation/maps-static/start) and [Geocoding](https://developers.google.com/maps/documentation/geocoding/start) APIs. | [`SemSeg on Google Maps`](./roofai/google_maps/semseg) [![image](https://github.com/kamangir/assets/raw/main/roofAI/roboflow/labelling-2.png?raw=true)](./roofai/google_maps/semseg) Google Maps semantic segmentation datasets and models. |

---


[![pylint](https://github.com/kamangir/roofai/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/roofai/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/roofai/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/roofai/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/roofai/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/roofai/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/roofai.svg)](https://pypi.org/project/roofai/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/roofai)](https://pypistats.org/packages/roofai)

built by 🌀 [`blue_options-4.223.1`](https://github.com/kamangir/awesome-bash-cli), based on 🏛️ [`roofai-6.230.1`](https://github.com/kamangir/roofai).
