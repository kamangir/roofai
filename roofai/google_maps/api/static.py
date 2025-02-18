from typing import Union, Dict
import requests
from PIL import Image
import numpy as np
import io
import math

from blueness import module
from blue_options import string

from roofai import NAME
from roofai.env import GOOGLE_MAPS_API_KEY
from roofai.google_maps.semseg.utils import meters_to_degrees
from roofai.logger import logger

NAME = module.name(__file__, NAME)

base_url = "https://maps.googleapis.com/maps/api/staticmap?"


# https://developers.google.com/maps/documentation/maps-static/start
def get(
    lat: float,
    lon: float,
    filename: str = "",
    zoom: int = 20,
    maptype: str = "satellite",
    size: str = "640x640",
) -> Union[bool, np.ndarray, Dict]:
    image: np.ndarray = np.array(())

    params = {
        "center": f"{lat},{lon}",
        "zoom": zoom,
        "size": size,
        "maptype": maptype,
        "key": GOOGLE_MAPS_API_KEY,
    }
    logger.info(
        "{}.get: {}".format(
            NAME,
            ", ".join(
                [f"{key}:{value}" for key, value in params.items() if key != "key"]
            ),
        )
    )

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        logger.error(
            "status_code={}, text={}".format(
                response.status_code,
                response.text,
            )
        )
        return False, image, {}

    try:
        image = np.array(Image.open(io.BytesIO(response.content)).convert("RGB"))
    except Exception as e:
        logger.error(e)
        return False, image, {}
    logger.info("image: {}".format(string.pretty_shape_of_matrix(image)))

    if filename:
        try:
            with open(filename, "wb") as file:
                file.write(response.content)
        except Exception as e:
            logger.error(e)
            return False, image, {}

        logger.info(f"-> {filename}")

    # https://groups.google.com/g/google-maps-js-api-v3/c/hDRO4oHVSeM?pli=1
    gsd = 156543.03392 * math.cos(lat * np.pi / 180) / (2**zoom)
    logger.info(f"gsd: {gsd:.2f} m")
    metadata = {"gsd": gsd}

    chip_height, chip_width = [int(piece) for piece in size.split("x")]
    if image.shape[0] != chip_height or image.shape[1] != chip_width:
        logger.warning(
            "image size mismatch: {} != {}x{}".format(
                string.pretty_shape_of_matrix(image),
                chip_height,
                chip_width,
            )
        )

    chip_height_in_meters = gsd * chip_height
    chip_width_in_meters = gsd * chip_width

    chip_height_in_degrees = meters_to_degrees(
        lat=lat,
        delta_in_m=chip_width_in_meters,
        direction="lat",
    )
    chip_width_in_degrees = meters_to_degrees(
        lat=lat,
        delta_in_m=chip_width_in_meters,
        direction="lon",
    )

    metadata["size"] = {
        "px": [chip_height, chip_width],
        "m": [chip_height_in_meters, chip_width_in_meters],
        "deg": [chip_height_in_degrees, chip_width_in_degrees],
    }
    logger.info(
        " = ".join(
            [
                "image size",
                "{} px x {} px".format(
                    chip_height,
                    chip_width,
                ),
                "{:,.2f} m x {:,.2f} m".format(
                    chip_height_in_meters,
                    chip_width_in_meters,
                ),
                "{:.5f} deg x {:.5f} deg ".format(
                    chip_height_in_degrees,
                    chip_width_in_degrees,
                ),
            ]
        )
    )

    return True, image, metadata
