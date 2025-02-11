import os

from blue_objects import objects, file


def cache_pretrainedmodels() -> bool:
    HOME = os.getenv("HOME")

    filename = f"{HOME}/.cache/torch/hub/checkpoints/se_resnext50_32x4d-a260b3a4.pth"

    model_name = file.name(filename)

    if not objects.download(model_name):
        return False

    return file.copy(
        objects.path_of(
            filename=f"{model_name}.pth",
            object_name=model_name,
        ),
        filename,
        overwrite=False,
    )
