import pytest
import numpy as np

from blue_objects import objects

from roofai import env
from roofai.tests.caching import cache_pretrainedmodels
from roofai.semseg import Profile
from roofai.google_maps.semseg.predict import predict


@pytest.mark.parametrize(
    ["lat", "lon"],
    [
        [
            env.ROOFAI_TEST_GOOGLE_MAPS_HOUSE_LAT,
            env.ROOFAI_TEST_GOOGLE_MAPS_HOUSE_LON,
        ],
    ],
)
def test_google_maps_predict(
    lat: float,
    lon: float,
):
    assert cache_pretrainedmodels()

    prediction_object_name = objects.unique_object("test_google_maps_predict")

    model_object_name = env.ROOFAI_DEFAULT_GOOGLE_MAPS_MODEL
    assert objects.download(model_object_name)

    success, output_image, input_image = predict(
        lat=lat,
        lon=lon,
        model_object_name=model_object_name,
        prediction_object_name=prediction_object_name,
        device="cpu",
        profile=Profile.VALIDATION,
    )
    assert success
    assert isinstance(output_image, np.ndarray)
    assert isinstance(input_image, np.ndarray)
