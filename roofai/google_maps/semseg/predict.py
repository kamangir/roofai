from typing import List, Tuple
import segmentation_models_pytorch as smp
import numpy as np
from tqdm import tqdm
import torch
import cv2

from blueness import module
from blue_options import string
from blue_options.elapsed_timer import ElapsedTimer
from blue_objects import objects, file
from blue_objects.mlflow.tags import get_tags
from blue_objects.metadata import post_to_object
from blue_objects.logger.matrix import log_matrix

from roofai import NAME
from roofai import fullname
from roofai.google_maps.api.geocoding import geocode
from roofai.google_maps.semseg.dataset import GoogleMapsDataset
from roofai.semseg import Profile
from roofai.semseg.augmentation import get_validation_augmentation, get_preprocessing
from roofai.semseg.model import SemSegModel
from roofai.logger import logger


NAME = module.name(__file__, NAME)


def predict(
    model_object_name: str,
    prediction_object_name: str,
    device: str,
    lat: float = 0.0,
    lon: float = 0.0,
    address: str = "",
    profile: Profile = Profile.VALIDATION,
    in_notebook: bool = False,
    batch_size: int = 32,
    verbose: bool = False,
) -> Tuple[bool, np.ndarray, np.ndarray]:
    output_matrix: np.ndarray = np.array(())
    input_matrix: np.ndarray = np.array(())

    if address:
        success, lat, lon, _ = geocode(
            address=address,
            object_name=prediction_object_name,
            verbose=verbose,
        )
        if not success:
            return success, output_matrix, input_matrix

    success, model_tags = get_tags(model_object_name)
    if not success:
        return success, output_matrix, input_matrix
    dataset_object_name = model_tags.get("dataset", "")
    if not dataset_object_name:
        logger.error(f"{model_object_name}.dataset not found.")
        return False, output_matrix, input_matrix

    success, dataset_tags = get_tags(dataset_object_name)
    if not success:
        return success, output_matrix, input_matrix
    zoom_str = dataset_tags.get("zoom", "bad-zoom-value")
    try:
        zoom = int(zoom_str)
    except Exception as e:
        logger.error(e)
        return False, output_matrix, input_matrix

    model = SemSegModel(
        model_filename=objects.path_of(
            filename="model.pth",
            object_name=model_object_name,
        ),
        profile=profile,
        device=device,
    )

    logger.info(
        "{}.predict: {}{:.05f},{:.05f} zoom={} -{}-batch-size:{}-> {}".format(
            NAME,
            f'"{address}" @ ' if address else "",
            lat,
            lon,
            zoom,
            device,
            batch_size,
            prediction_object_name,
        )
    )

    preprocessing_fn = smp.encoders.get_preprocessing_fn(
        model.encoder_name,
        model.encoder_weights,
    )

    dataset = GoogleMapsDataset(
        lat=lat,
        lon=lon,
        zoom=zoom,
        augmentation=get_validation_augmentation(),
        preprocessing=get_preprocessing(preprocessing_fn),
        count=model.profile.data_count,
        prediction_object_name=prediction_object_name,
        verbose=verbose,
    )

    index_list = (
        [np.random.choice(len(dataset))]
        if model.profile == Profile.VALIDATION
        else range(len(dataset))
    )
    timer = ElapsedTimer()
    list_of_masks: List[np.ndarray] = []
    for i in tqdm(range(0, len(index_list), batch_size)):
        batch_indices = index_list[i : i + batch_size]
        images = [dataset[n][0] for n in batch_indices]

        x_tensor = torch.from_numpy(np.stack(images)).to(model.device)
        pr_masks = model.model.predict(x_tensor)
        pr_masks = pr_masks.cpu().numpy()
        list_of_masks += [pr_masks]
    timer.stop()
    logger.info(f"took {timer.elapsed_pretty()}")

    stack_of_masks = np.concatenate(list_of_masks, axis=0)

    chip_count = stack_of_masks.shape[0]
    logger.info(f"stitching {chip_count:,} chip(s)...")
    output_matrix = np.zeros(dataset.matrix.shape[:2], dtype=np.float32)
    weight_matrix = np.zeros(dataset.matrix.shape[:2], dtype=np.uint8)
    chip_index: int = 0
    for y in range(
        dataset.chip_height_offset,
        dataset.matrix.shape[0] - dataset.chip_height + dataset.chip_height_offset,
        dataset.chip_height_overlap,
    ):
        for x in range(
            dataset.chip_width_offset,
            dataset.matrix.shape[1] - dataset.chip_width + dataset.chip_width_offset,
            dataset.chip_width_overlap,
        ):
            output_matrix[
                y : y + dataset.chip_height,
                x : x + dataset.chip_width,
            ] += stack_of_masks[chip_index, 0]

            weight_matrix[
                y : y + dataset.chip_height,
                x : x + dataset.chip_width,
            ] += 1

            chip_index += 1
            if chip_index >= len(dataset):
                break
        if chip_index >= len(dataset):
            break

    output_filename = objects.path_of(
        filename="prediction.png",
        object_name=prediction_object_name,
        create=True,
    )

    weight_matrix[weight_matrix == 0] = 1  # output_matrix is zero at them anyways :)
    output_matrix = output_matrix / weight_matrix

    if not log_matrix(
        matrix=output_matrix,
        suffix=[dataset.matrix],
        header=objects.signature(
            info="prediction",
            object_name=prediction_object_name,
        )
        + ([address] if address else [])
        + [
            f"lat:{lat:.05f}",
            f"lon:{lon:.05f}",
            f"model: {model_object_name}",
            model.signature,
            f"device: {device}",
            f"profile: {profile}",
            f"batch_size: {batch_size}",
            "took {}".format(
                timer.elapsed_pretty(
                    largest=True,
                    short=True,
                )
            ),
            f"{chip_count:,} chip(s)",
        ],
        footer=[fullname()],
        dynamic_range=[0, 1.0],
        filename=file.add_extension(output_filename, "png"),
        colormap=cv2.COLORMAP_JET,
        verbose=True,
    ):
        return False, output_matrix, dataset.matrix

    output_matrix = output_matrix * 255
    output_matrix[output_matrix < 0] = 0
    output_matrix[output_matrix > 255] = 255
    output_matrix = output_matrix.astype(np.uint8)

    return (
        post_to_object(
            prediction_object_name,
            NAME.replace(".", "-"),
            {
                "lat": lat,
                "lon": lon,
                "chip_count": chip_count,
                "creation-date": string.pretty_date(),
                "address": address,
                "elapsed_time": timer.elapsed_time,
                "model": model_object_name,
                "output_filename": file.name_and_extension(output_filename),
            },
        ),
        output_matrix,
        dataset.matrix,
    )
