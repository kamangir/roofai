from typing import Dict, Tuple
import requests

from blueness import module
from blue_objects.metadata import post_to_object

from roofai import NAME
from roofai.env import GOOGLE_MAPS_API_KEY
from roofai.logger import logger

NAME = module.name(__file__, NAME)

# https://developers.google.com/maps/documentation/geocoding/start
base_url = "https://maps.googleapis.com/maps/api/geocode/json?"


def geocode(
    address: str,
    object_name: str = "",
    verbose: bool = False,
) -> Tuple[bool, float, float, Dict]:
    success = True

    params = {
        "address": address,
        "key": GOOGLE_MAPS_API_KEY,
    }
    logger.info(f"{NAME}.geocode({address})")

    response = requests.get(base_url, params=params)

    description_of_failure: str = ""
    metadata: Dict = {}
    lat: float = 0.0
    lon: float = 0.0
    if response.status_code != 200:
        success = False
        description_of_failure = "status_code={}, text={}".format(
            response.status_code,
            response.text,
        )

    if success:
        metadata = response.json()
        if verbose:
            logger.info(metadata)

        if metadata["status"] != "OK":
            success = False
            description_of_failure = "status={}".format(
                metadata["status"],
            )

    if success:
        if len(metadata["results"]) == 0:
            success = False
            description_of_failure = "no results found"
        elif len(metadata["results"]) > 1:
            logger.warning(
                "{} result(s), using the first one.".format(len(metadata["results"]))
            )

    if success:
        try:
            lat = metadata["results"][0]["geometry"]["location"]["lat"]
            lon = metadata["results"][0]["geometry"]["location"]["lng"]
        except Exception as e:
            success = False
            description_of_failure = str(e)

    if not success:
        logger.error(
            "{}.geocode({}) failed: {}".format(
                NAME,
                address,
                description_of_failure,
            )
        )
        return False, 0, 0, {"error": description_of_failure}

    logger.info(
        "{}.geocode({}): lat:{:.6f}, lon:{:.6f}".format(
            NAME,
            address,
            lat,
            lon,
        )
    )

    if object_name:
        success = post_to_object(
            object_name,
            "geocoding",
            {
                "address": address,
                "lat": lat,
                "lon": lon,
                "metadata": metadata,
            },
        )

    return success, lat, lon, metadata
