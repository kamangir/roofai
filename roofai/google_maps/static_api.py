from typing import Union
import requests
from PIL import Image
import numpy as np
import io

from blueness import module
from blue_options import string

from roofai import NAME
from roofai.env import GOOGLE_MAPS_API_KEY
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
) -> Union[bool, np.ndarray]:
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
        return False, image

    try:
        image = np.array(Image.open(io.BytesIO(response.content)))
    except Exception as e:
        logger.error(e)
        return False, image
    logger.info(string.pretty_shape_of_matrix(image))

    if filename:
        try:
            with open(filename, "wb") as file:
                file.write(response.content)
        except Exception as e:
            logger.error(e)
            return False, image

        logger.info(f"-> {filename}")

    return True, image
