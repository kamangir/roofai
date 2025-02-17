from typing import List

from blue_options.terminal import show_usage, xtra

from roofai.help.roboflow import upload_options


def help_ingest_AIRS_or_distributed(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("download,dryrun,", mono=mono),
            "source=<source>",
            xtra(",target=<target>,upload", mono=mono),
        ]
    )

    args = [
        "[--test_count <10>]",
        "[--train_count <80>]",
        "[--val_count <10>]",
    ]

    return show_usage(
        [
            "roofai",
            "dataset",
            "ingest",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "ingest <source> -> <object-name>.",
        {
            "source: AIRS | <query-object-name>": [],
            "target: sagemaker | torch": [],
        },
        mono=mono,
    )


def help_ingest_CamVid(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "source=CamVid",
            xtra(",upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "roofai",
            "dataset",
            "ingest",
            f"[{options}]",
            "[-|<object-name>]",
        ],
        "ingest CamVid -> <object-name>.",
        mono=mono,
    )


def help_ingest_gmaps(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "source=gmaps",
            xtra(",upload", mono=mono),
        ]
    )

    ingest_options = "count=<count>,lat=<lat>,lon=<lon>,zoom=<zoom>"

    roboflow_options = "roboflow,{}".format(
        upload_options(
            mono=mono,
            cascade=True,
        )
    )

    return show_usage(
        [
            "roofai",
            "dataset",
            "ingest",
            f"[{options}]",
            "[-|<object-name>]",
            f"[{ingest_options}]",
            f"[{roboflow_options}]",
        ],
        "ingest gmaps -> <object-name> -> roboflow/<project-name>.",
        mono=mono,
    )


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    return "\n".join(
        [
            help_ingest_AIRS_or_distributed(tokens, mono),
            help_ingest_CamVid(tokens, mono),
            help_ingest_gmaps(tokens, mono),
        ]
    )


def help_review(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "download",
            xtra(",dryrun", mono=mono),
        ]
    )

    args = [
        "[--count <1>]",
        "[--index <index>]",
        "[--subset <subset>]",
    ]

    return show_usage(
        [
            "roofai",
            "dataset",
            "review",
            f"[{options}]",
            "[.|<object-name>]",
        ]
        + args,
        "review <object-name>.",
        mono=mono,
    )


help_functions = {
    "ingest": help_ingest,
    "review": help_review,
}
