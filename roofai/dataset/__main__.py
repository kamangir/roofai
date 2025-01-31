import argparse
from tqdm import trange

from blueness import module
from blueness.argparse.generic import sys_exit

from roofai import NAME
from roofai.dataset.classes import RoofAIDataset
from roofai.dataset.classes import DatasetTarget
from roofai.dataset.ingest.from_dataset import ingest_from_dataset
from roofai.dataset.ingest.CamVid import ingest_CamVid
from roofai.logger import logger


NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="ingest|review",
)
parser.add_argument(
    "--input_dataset_path",
    type=str,
    default="",
)
parser.add_argument(
    "--count",
    type=int,
    default=1,
)
parser.add_argument(
    "--dataset_path",
    type=str,
    default="",
)
parser.add_argument(
    "--description",
    type=str,
    help="line1,line2",
    default="",
)
parser.add_argument(
    "--index",
    type=int,
    default=10,
)
parser.add_argument(
    "--output_dataset_path",
    type=str,
    default="",
)
parser.add_argument(
    "--log",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--source",
    type=str,
    default="",
    help="AIRS|CamVid",
)
parser.add_argument(
    "--target",
    type=str,
    default="torch",
    help="torch|sagemaker",
)
parser.add_argument(
    "--subset",
    type=str,
    default="test",
)
parser.add_argument(
    "--test_count",
    type=int,
    default=10,
)
parser.add_argument(
    "--train_count",
    type=int,
    default=10,
)
parser.add_argument(
    "--val_count",
    type=int,
    default=10,
)
parser.add_argument(
    "--is_distributed",
    type=int,
    default=0,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "ingest":
    if args.source == "AIRS" or args.is_distributed == 1:
        success = ingest_from_dataset(
            input_dataset_path=args.input_dataset_path,
            output_dataset_path=args.output_dataset_path,
            counts={
                "test": args.test_count,
                "train": args.train_count,
                "val": args.val_count,
            },
            target=DatasetTarget[args.target.upper()],
            log=args.log,
            is_distributed=args.is_distributed,
            verbose=args.verbose,
        )
    elif args.source == "CamVid":
        success = ingest_CamVid(
            output_dataset_path=args.output_dataset_path,
        )
    else:
        logger.error(f"-{NAME}: {args.task}: {args.source}: source not found.")
elif args.task == "review":
    dataset = RoofAIDataset(args.dataset_path)

    for index in trange(args.count):
        dataset.visualize(
            subset=args.subset,
            index=index + args.index,
            in_notebook=False,
            description=args.description.split(","),
            log=args.log,
        )

    success = True
else:
    success = None

sys_exit(logger, NAME, args.task, success)
