from typing import List

from blue_options.terminal import show_usage, xtra

from roofai.semseg import Profile

list_of_profiles = [profile.name for profile in Profile]

device_and_profile_details = {
    "device: cpu | cuda": [],
    "profile: {}".format(" | ".join(list_of_profiles)): [],
}


def predict_options(
    mono: bool,
    cascade: bool = False,
):
    return "".join(
        [
            xtra(
                "device=<device>,{}profile=<profile>,".format(
                    "~download,dryrun," if not cascade else ""
                ),
                mono=mono,
            ),
            "upload",
        ]
    )


def help_predict(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "roofai",
            "semseg",
            "predict",
            f"[{predict_options(mono=mono)}]",
            "[..|<model-object-name>]",
            "[.|<dataset-object-name>]",
            "[-|<prediction-object-name>]",
        ],
        "semseg[<model-object-name>].predict(<dataset-object-name>) -> <prediction-object-name>.",
        device_and_profile_details,
        mono=mono,
    )


def train_options(
    mono: bool,
    show_download: bool = True,
):
    return "".join(
        [
            xtra(
                "device=<device>,{}dryrun,profile=<profile>,".format(
                    "~download," if show_download else ""
                ),
                mono=mono,
            ),
            "upload",
        ]
    )


def help_train(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--activation <sigmoid>]",
        "[--classes <one+two+three+four>]",
        "[--encoder_name <se_resnext50_32x4d>]",
        "[--encoder_weights <imagenet>]",
        "[--epoch_count <-1>]",
    ]

    return show_usage(
        [
            "roofai",
            "semseg",
            "train",
            f"[{train_options(mono=mono)}]",
            "[.|<dataset-object-name>]",
            "[-|<model-object-name>]",
        ]
        + args,
        "semseg.train(<dataset-object-name>) -> <model-object-name>.",
        device_and_profile_details,
        mono=mono,
    )


help_functions = {
    "predict": help_predict,
    "train": help_train,
}
