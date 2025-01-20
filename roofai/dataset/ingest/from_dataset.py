import os
from tqdm import tqdm, trange
from typing import List, Tuple, Dict
import numpy as np
import matplotlib.pyplot as plt
import random
import glob

from blueness import module
from blue_options import string
from blue_objects import file, path


from roofai import NAME, VERSION
from roofai.dataset.classes import RoofAIDataset, DatasetKind, MatrixKind, DatasetTarget
from roofai.logger import logger

NAME = module.name(__file__, NAME)


def ingest_from_dataset(
    input_dataset_path: str,
    output_dataset_path: str,
    counts: Dict[str, int],
    chip_overlap: float = 0.25,
    log: bool = False,
    verbose: bool = False,
    in_notebook: bool = False,
    target: DatasetTarget = DatasetTarget.TORCH,
    is_distributed: bool = False,
) -> bool:
    chip_height = target.chip_height
    chip_width = target.chip_width

    input_object_name = path.name(input_dataset_path)
    output_object_name = path.name(output_dataset_path)

    logger.info(
        "ingesting from {}{} -{}-{}x{}-@{:.0f}%-> {}:{}".format(
            input_object_name,
            " (distributed)" if is_distributed else "",
            " + ".join(
                ["{} X {:,d}".format(subset, count) for subset, count in counts.items()]
            ),
            chip_height,
            chip_width,
            chip_overlap * 100,
            target.name.lower(),
            output_object_name,
        )
    )

    original_counts = {class_name: count for class_name, count in counts.items()}
    if is_distributed:
        total_count = sum([count for count in counts.values()])
        counts = {
            class_name: total_count if class_name == "train" else 0
            for class_name, count in counts.items()
        }
        logger.info(f"☁️ distributed dataset, will ingest {total_count:,} chips first.")

    input_dataset = RoofAIDataset(input_dataset_path)
    output_dataset = RoofAIDataset(
        output_dataset_path,
        kind=(
            DatasetKind.CAMVID
            if target == DatasetTarget.TORCH
            else DatasetKind.SAGEMAKER
        ),
    ).create(log=log)

    output_dataset.classes = [class_name for class_name in input_dataset.classes]

    train_record_id_list = []
    for subset in tqdm(counts.keys()):
        record_id_list = []
        for matrix_kind in [MatrixKind.MASK, MatrixKind.IMAGE]:  # order is critical.
            chip_count = counts[subset]
            for record_id in input_dataset.subsets[subset]:
                input_matrix = input_dataset.get_matrix(
                    subset,
                    record_id,
                    matrix_kind,
                    log=log,
                )

                slice_count, slice_record_id_list = slice_matrix(
                    input_matrix=input_matrix,
                    kind=matrix_kind,
                    chip_height=chip_height,
                    chip_width=chip_width,
                    chip_overlap=chip_overlap,
                    max_chip_count=chip_count,
                    record_id_list=record_id_list,
                    output_path=output_dataset.subset_path(subset, matrix_kind),
                    target=target,
                    prefix=record_id,
                    log=log,
                    verbose=verbose,
                    class_count=len(output_dataset.classes),
                )

                chip_count -= slice_count

                record_id_list = list(set(record_id_list + slice_record_id_list))

                if chip_count <= 0:
                    break
                if log:
                    logger.info(f"remaining chip count: {chip_count:,}")

        if subset == "train":
            train_record_id_list = [record_id for record_id in record_id_list]

    if is_distributed:
        counts = {
            class_name: (
                int(original_count / total_count * len(train_record_id_list))
                if total_count
                else 0
            )
            for class_name, original_count in original_counts.items()
        }
        logger.info(
            "splitting {:,} chips to {}".format(
                len(train_record_id_list),
                " + ".join(
                    [f"{class_name}:{count:,}" for class_name, count in counts.items()]
                ),
            )
        )

        random.shuffle(train_record_id_list)

        global_record_index = counts["train"]
        for subset in tqdm(counts.keys()):
            if subset == "train":
                continue

            next_global_record_index = global_record_index + counts[subset]
            for record_index in trange(
                global_record_index,
                next_global_record_index,
            ):
                record_id = train_record_id_list[record_index]

                for matrix_kind in [MatrixKind.MASK, MatrixKind.IMAGE]:
                    path_pairs: Dict[str, str] = {
                        output_dataset.subset_path(
                            "train", matrix_kind
                        ): output_dataset.subset_path(subset, matrix_kind)
                    }

                    if matrix_kind == MatrixKind.MASK:
                        path_pairs.update(
                            {
                                f"{source_path}-colored": f"{destination_path}-colored"
                                for source_path, destination_path in path_pairs.items()
                            }
                        )

                    for source_path, destination_path in path_pairs.items():
                        for filename in glob.glob(
                            os.path.join(
                                source_path,
                                f"{record_id}*.*",
                            )
                        ):
                            if not file.move(
                                filename,
                                destination=os.path.join(
                                    destination_path,
                                    file.name_and_extension(filename),
                                ),
                            ):
                                return False

            global_record_index = next_global_record_index

    file.save_yaml(
        os.path.join(output_dataset_path, "metadata.yaml"),
        {
            "classes": output_dataset.classes,
            "kind": "CamVid" if target == DatasetTarget.TORCH else "SageMaker",
            "source": input_object_name if is_distributed else "AIRS",
            "ingested-by": f"{NAME}-{VERSION}",
            # SageMaker
            "bucket": "kamangir",
            "channel": (
                {
                    "label_map": f"s3://kamangir/bolt/{output_object_name}/label_map/train_label_map.json",
                    "train": f"s3://kamangir/bolt/{output_object_name}/train",
                    "train_annotation": f"s3://kamangir/bolt/{output_object_name}/train_annotation",
                    "validation": f"s3://kamangir/bolt/{output_object_name}/validation",
                    "validation_annotation": f"s3://kamangir/bolt/{output_object_name}/validation_annotation",
                }
                if target == DatasetTarget.SAGEMAKER
                else {}
            ),
            "num": counts,
            "prefix": f"bolt/{output_object_name}",
        },
        log=True,
    )

    RoofAIDataset(output_dataset_path).visualize(
        subset="train",
        index=0,
        in_notebook=in_notebook,
    )

    return True


def slice_matrix(
    input_matrix: np.ndarray,
    kind: MatrixKind,
    chip_height: int,
    chip_width: int,
    chip_overlap: float,
    max_chip_count: int,
    record_id_list: List[str],
    output_path: str,
    prefix: str,
    class_count: int,
    target: DatasetTarget = DatasetTarget.TORCH,
    log: bool = True,
    verbose: bool = False,
) -> Tuple[int, List[str]]:
    if log:
        logger.info(
            "slice_matrix[{}]: {} -{}X{}x{}-@{:.0f}%-> {} - {}{}".format(
                string.pretty_shape_of_matrix(input_matrix),
                kind,
                max_chip_count,
                chip_height,
                chip_width,
                chip_overlap * 100,
                output_path,
                prefix,
                (
                    ""
                    if kind == MatrixKind.MASK
                    else ": {} record_id(s): {}".format(
                        len(record_id_list),
                        ", ".join(record_id_list[:3] + ["..."]),
                    )
                ),
            )
        )

    record_id_list_output = []

    count = 0
    for y in range(
        0, input_matrix.shape[0] - chip_height, int(chip_overlap * chip_height)
    ):
        for x in range(
            0, input_matrix.shape[1] - chip_width, int(chip_overlap * chip_width)
        ):
            chip = input_matrix[
                y : y + chip_height,
                x : x + chip_width,
            ]

            record_id = f"{prefix}-{y:05d}-{x:05d}"

            # to ensure variety of labels in the pixel.
            # TODO: make it more elaborate.
            if (kind == MatrixKind.MASK and np.all(chip == 0)) or (
                kind == MatrixKind.IMAGE and (record_id not in record_id_list)
            ):
                continue
            record_id_list_output += [record_id]

            assert file.save_image(
                os.path.join(
                    output_path,
                    "{}.{}".format(
                        record_id,
                        (
                            "jpg"
                            if (kind == MatrixKind.IMAGE)
                            and (target == DatasetTarget.SAGEMAKER)
                            else "png"
                        ),
                    ),
                ),
                chip,
                log=verbose,
            )

            if kind == MatrixKind.MASK:
                assert file.save_image(
                    os.path.join(
                        path.parent(output_path),
                        f"{path.name(output_path)}-colored",
                        f"{record_id}.png",
                    ),
                    (
                        plt.cm.viridis(chip.astype(np.float32) / class_count) * 255
                    ).astype(np.uint8)[:, :, :3],
                    log=verbose,
                )

            count += 1
            if count >= max_chip_count:
                return count, record_id_list_output

    return count, record_id_list_output
