import pytest
import numpy as np

from blue_options import string
from blue_objects import objects

from roofai import env
from roofai.google_maps.static_api import get as get_static_image


@pytest.mark.parametrize(
    ["lat"],
    [[env.ROOFAI_TEST_GOOGLE_MAPS_LAT]],
)
@pytest.mark.parametrize(
    ["lon"],
    [[env.ROOFAI_TEST_GOOGLE_MAPS_LON]],
)
def test_google_maps_get_static_image(
    lat: float,
    lon: float,
):
    object_name = objects.unique_object("test_google_maps_get_static_image")

    success, image = get_static_image(
        lat=lat,
        lon=lon,
        filename=objects.path_of(
            object_name=object_name,
            filename=f"{string.timestamp()}.png",
        ),
    )

    assert success
    assert isinstance(image, np.ndarray)
