from blueness import module

from roofai import NAME
from roofai.env import GOOGLE_MAPS_API_KEY
from roofai.logger import logger

NAME = module.name(__file__, NAME)


def ingest_dataset(
    lat: float,
    lon: float,
    zoom: int,
    count: int,
    object_name: str,
) -> bool:
    logger.info(
        "{}.ingest_dataset: [lat={:.6f}, lon={:.6f}] @ zoom={} * count={} -> {}".format(
            NAME,
            lat,
            lon,
            zoom,
            count,
            object_name,
        )
    )

    logger.info("🪄")

    return True
