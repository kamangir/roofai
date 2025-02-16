import math
from tqdm import trange

from blueness import module
from blue_objects import objects
from blue_objects.metadata import post_to_object

from roofai import NAME
from roofai.google_maps.api.static import get as get_static_image
from roofai.google_maps.semseg.utils import meters_to_degrees
from roofai.logger import logger

NAME = module.name(__file__, NAME)


def ingest_dataset(
    lat: float,
    lon: float,
    zoom: int,
    maptype: str,
    size: str,
    count: int,
    object_name: str,
) -> bool:
    if count < 1:
        return False

    metadata = {
        "lat": lat,
        "lon": lon,
        "zoom": zoom,
        "maptype": maptype,
        "size": size,
        "count": count,
    }

    logger.info(
        "{}.ingest_dataset: [lat={:.6f}, lon={:.6f}] of {} @ zoom={} * count={} * {} -> {}".format(
            NAME,
            lat,
            lon,
            maptype,
            zoom,
            count,
            size,
            object_name,
        )
    )

    success, _, metadata["center"] = get_static_image(
        lat=lat,
        lon=lon,
        zoom=zoom,
        maptype=maptype,
        size=size,
    )
    if not success:
        return False

    width_count = int(math.ceil(math.sqrt(count)))
    height_count = int(math.ceil(count / width_count))
    logger.info(f"grid: {height_count}x{width_count}")
    metadata["grid"] = [height_count, width_count]

    chip_height_in_degrees, chip_width_in_degrees = metadata["center"]["size"]["deg"]

    lat_0 = lat - width_count / 2 * chip_width_in_degrees
    lon_0 = lon - height_count / 2 * chip_height_in_degrees

    for x in trange(width_count):
        for y in range(height_count):
            filename = objects.path_of(
                object_name=object_name,
                filename=f"{x:05d}-{y:05d}.png",
            )

            lat_xy = lat_0 + x * chip_width_in_degrees
            lon_xy = lon_0 + y * chip_height_in_degrees

            success, _, _ = get_static_image(
                lat=lat_xy,
                lon=lon_xy,
                filename=filename,
                zoom=zoom,
                maptype=maptype,
                size=size,
            )
            if not success:
                return False

    return post_to_object(
        object_name,
        NAME.replace(".", "-"),
        metadata,
    )
