import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from blue_objects import objects

from roofai import NAME
from roofai.google_maps.geocoding import geocode
from roofai.google_maps.static_api import get as get_static_image
from roofai.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="get_static_image | geocode",
)
parser.add_argument(
    "--lat",
    type=float,
    default=0,
)
parser.add_argument(
    "--lon",
    type=float,
    default=0,
)
parser.add_argument(
    "--filename",
    type=str,
    default="",
)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--zoom",
    type=int,
    default=20,
)
parser.add_argument(
    "--maptype",
    type=str,
    default="satellite",
)
parser.add_argument(
    "--size",
    type=str,
    default="640x640",
)
parser.add_argument(
    "--address",
    type=str,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "get_static_image":
    success, _, _ = get_static_image(
        lat=args.lat,
        lon=args.lon,
        filename=(
            objects.path_of(
                object_name=args.object_name,
                filename=args.filename,
            )
            if args.filename
            else ""
        ),
        zoom=args.zoom,
        maptype=args.maptype,
        size=args.size,
    )
elif args.task == "geocode":
    success, _, _, _ = geocode(
        address=args.address,
        object_name=args.object_name,
        verbose=args.verbose == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
