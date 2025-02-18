from typing import List
import numpy as np
from torch.utils.data import Dataset as BaseDataset

from blueness import module
from blue_objects import file, objects

from roofai.dataset.classes import DatasetTarget
from roofai.google_maps.api.static import get as get_static_image
from roofai import NAME
from roofai.logger import logger

NAME = module.name(__file__, NAME)


class GoogleMapsDataset(BaseDataset):
    def __init__(
        self,
        lat: float,
        lon: float,
        zoom: int,
        augmentation=None,
        preprocessing=None,
        count=-1,
        chip_overlap: float = 0.25,
        prediction_object_name: str = "",
        size: str = "640x640",
        verbose: bool = False,
    ):

        self.chip_height = DatasetTarget.TORCH.chip_height
        self.chip_width = DatasetTarget.TORCH.chip_width
        self.chip_overlap = chip_overlap

        success, self.matrix, _ = get_static_image(
            lat=lat,
            lon=lon,
            filename=(
                objects.path_of(
                    object_name=prediction_object_name,
                    filename="input.png",
                )
                if verbose
                else ""
            ),
            zoom=zoom,
            maptype="satellite",
            size=size,
        )
        assert success

        self.ids: List[str] = []
        for y in range(
            self.chip_height_offset,
            self.matrix.shape[0] - self.chip_height + self.chip_height_offset,
            self.chip_height_overlap,
        ):
            for x in range(
                self.chip_width_offset,
                self.matrix.shape[1] - self.chip_width + self.chip_width_offset,
                self.chip_width_overlap,
            ):
                self.ids += [f"{y:05d}-{x:05d}"]

        if count != -1:
            self.ids = self.ids[:count]

        self.augmentation = augmentation
        self.preprocessing = preprocessing

        logger.info(
            "{}.GoogleMapsDataset({:.05f},{:.05f}, zoom={}): {:,} chip(s) x {}x{}.".format(
                NAME,
                lat,
                lon,
                zoom,
                len(self.ids),
                self.chip_height,
                self.chip_width,
            )
        )

    @property
    def chip_width_offset(self):
        return int(
            ((self.matrix.shape[1] - self.chip_width) % self.chip_width_overlap) / 2
        )

    @property
    def chip_width_overlap(self):
        return int(self.chip_overlap * self.chip_width)

    @property
    def chip_height_offset(self):
        return int(
            ((self.matrix.shape[0] - self.chip_height) % self.chip_height_overlap) / 2
        )

    @property
    def chip_height_overlap(self):
        return int(self.chip_overlap * self.chip_height)

    def __getitem__(self, i):
        item_id = self.ids[i]  # expecting f"{y:05d}-{x:05d}"

        pieces = item_id.split("-")
        assert len(pieces) == 2
        y = int(pieces[0])
        x = int(pieces[1])

        image = self.matrix[
            y : y + self.chip_height,
            x : x + self.chip_width,
        ]

        mask = np.zeros(image.shape, dtype=np.uint8)

        if self.augmentation:
            sample = self.augmentation(image=image, mask=mask)
            image, mask = sample["image"], sample["mask"]

        if self.preprocessing:
            sample = self.preprocessing(image=image, mask=mask)
            image, mask = sample["image"], sample["mask"]

        return image, mask

    def __len__(self):
        return len(self.ids)
