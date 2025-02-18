from typing import List

from blue_options.terminal import show_usage

from roofai.help.semseg import predict_options


def help_predict(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "lat=<lat>,lon=<lon>"

    args = [
        "[--address <address>]",
    ]

    return show_usage(
        [
            "@gmaps",
            "predict",
            f"[{options}]",
            "[{}]".format(predict_options(mono=mono)),
            "[<model-object-name>]",
            "[-|<prediction-object-name>]",
        ]
        + args,
        "<lat>, <lon> -predict-> <prediction-object-name>.",
        mono=mono,
    )
