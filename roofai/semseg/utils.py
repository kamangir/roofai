import matplotlib.pyplot as plt
import numpy as np
from typing import List, Any

from blueness import module
from blue_options import string
from blue_objects import file, path, objects
from blue_objects.graphics.signature import sign_filename

from roofai import NAME
from roofai.host import signature


NAME = module.name(__file__, NAME)


# helper function for data visualization
def visualize(
    images,
    filename: str = "",
    in_notebook: bool = False,
    description: List[str] = [],
    list_of_contours: List[Any] = [],
    line_width: int = 80,
):
    n = len(images)
    fig = plt.figure(figsize=(n * 5, 5))

    for name in images:
        if isinstance(images[name], str):
            success, images[name] = image = file.load_image(images[name], log=True)
            assert success

    for name in images:
        images[name][np.isnan(images[name])] = 0

    for i, (name, image) in enumerate(images.items()):
        ax = fig.add_subplot(1, n, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.xlabel(
            "{} - {}{}".format(
                name,
                string.pretty_shape_of_matrix(image),
                (
                    " - {} levels: {}..{}".format(
                        len(np.unique(image)),
                        int(np.min(image)),
                        int(np.max(image)),
                    )
                    if name in "prediction,mask,groundtruth".split(",")
                    else ""
                ),
            )
        )
        ax.imshow(image)

        if name == "image":
            for contour in list_of_contours:
                plt.plot(
                    contour[0],
                    contour[1],
                    "o-",
                    color="orange",
                )

    if filename:
        file.prepare_for_saving(filename)
        plt.savefig(filename)
        success = sign_filename(
            filename,
            header=objects.signature(
                info=file.name(filename),
                object_name=path.name(file.path(filename)),
            )
            + description,
            footer=signature(),
            line_width=line_width,
        )

    if in_notebook:
        plt.show()
    plt.close()
