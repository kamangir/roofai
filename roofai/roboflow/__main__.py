import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from roofai import NAME
from roofai.roboflow.project import create_project
from roofai.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="create_project",
)
parser.add_argument(
    "--name",
    type=str,
)
parser.add_argument(
    "--description",
    type=str,
)
parser.add_argument(
    "--type",
    type=str,
    default="semantic-segmentation",
)
parser.add_argument(
    "--license",
    type=str,
    default="MIT",
)
args = parser.parse_args()

success = False
if args.task == "create_project":
    success = create_project(
        project_name=args.name,
        project_description=args.description,
        project_type=args.type,
        project_license=args.license,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
