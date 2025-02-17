import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from roofai import NAME
from roofai.roboflow.create import create_project
from roofai.roboflow.upload import upload_to_project
from roofai.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="create_project | upload",
)
parser.add_argument(
    "--project_name",
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
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--create",
    type=int,
    default=1,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "create_project":
    success = create_project(
        project_name=args.project_name,
        project_description=args.description,
        project_type=args.type,
        project_license=args.license,
    )
elif args.task == "upload":
    success = upload_to_project(
        object_name=args.object_name,
        project_name=args.project_name,
        create=args.create == 1,
        verbose=args.verbose == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
