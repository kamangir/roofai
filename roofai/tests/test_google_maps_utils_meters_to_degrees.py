import pytest
from roofai.google_maps.semseg.utils import meters_to_degrees


@pytest.mark.parametrize(
    ["direction"],
    [
        ["lat"],
        ["lon"],
    ],
)
def test_google_maps_utils_meters_to_degrees(direction: str):
    lat = 49.2827
    delta_in_m = 100

    output = meters_to_degrees(
        lat=lat,
        delta_in_m=delta_in_m,
        direction=direction,
    )
    assert isinstance(output, float)


def test_google_maps_utils_meters_to_degrees_exception():
    lat = 49.2827
    delta_in_m = 100
    direction = "void"

    with pytest.raises(ValueError):
        meters_to_degrees(
            lat=lat,
            delta_in_m=delta_in_m,
            direction=direction,
        )
