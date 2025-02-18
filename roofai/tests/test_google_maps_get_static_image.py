import pytest
import numpy as np

from blue_options import string
from blue_objects import objects

from roofai import env
from roofai.google_maps.api.static import get as get_static_image


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

    success, image, metadata = get_static_image(
        lat=lat,
        lon=lon,
        filename=objects.path_of(
            object_name=object_name,
            filename=f"{string.timestamp()}.png",
        ),
    )

    assert success
    assert isinstance(image, np.ndarray)
    assert len(image.shape) == 3
    assert image.shape[2] == 3

    assert "gsd" in metadata
    assert isinstance(metadata["gsd"], float)

    assert "size" in metadata
