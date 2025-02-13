import pytest
import numpy as np

from blue_options import string
from blue_objects import objects

from roofai import env
from roofai.google_maps.geocoding import geocode


@pytest.mark.parametrize(
    ["address", "expected_success"],
    [
        ["350 W Georgia St, Vancouver, BC V6B 6B1, Canada", True],
        ["void", False],
    ],
)
def test_google_maps_geocode(
    address: str,
    expected_success: bool,
):
    for object_name in [
        "",
        objects.unique_object("test_google_maps_geocode"),
    ]:
        success, lat, lon, _ = geocode(
            address=address,
            object_name=object_name,
            verbose=True,
        )
        assert success == expected_success

        if expected_success:
            assert isinstance(lat, float)
            assert isinstance(lon, float)
