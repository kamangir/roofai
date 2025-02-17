from typing import List

from blue_options.terminal import show_usage, xtra

from roofai.roboflow.create import list_of_project_types


project_type_details = {
    "type: {}".format(" | ".join(list_of_project_types)): [],
}


def help_create_project(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "project=<project-name>",
        ]
    )

    args = [
        "[--description <description>]",
        "[--type <type>]",
        "[--license <MIT>]",
    ]

    return show_usage(
        [
            "@roboflow",
            "create_project",
            f"[{options}]",
        ]
        + args,
        "create a roboflow project.",
        project_type_details,
        mono=mono,
    )


def help_download(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,~clean,", mono=mono),
            "project=<project-name>",
            xtra(",~review,", mono=mono),
            "upload,version=<version>",
        ]
    )

    ingest_options = "".join(
        [
            "ingest,count=<10000>",
            xtra(",dryrun,upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "@roboflow",
            "download",
            f"[{options}]",
            "[-|<object-name>]",
            f"[{ingest_options}]",
            "[-|<dataset-object-name>]",
        ],
        "download roboflow/<project-name> & ...",
        mono=mono,
    )


def upload_options(
    mono: bool,
    cascade: bool = False,
):
    return "".join(
        [
            xtra("~create,", mono=mono),
            "" if cascade else xtra("~download,", mono=mono),
            xtra("dryrun,", mono=mono),
            "project=<project-name>",
        ]
    )


def help_status(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "dryrun"

    return show_usage(
        [
            "@roboflow",
            "status",
            f"[{options}]",
        ],
        "show roboflow status.",
        mono=mono,
    )


def help_upload(
    tokens: List[str],
    mono: bool,
) -> str:
    options = upload_options(mono=mono)

    return show_usage(
        [
            "@roboflow",
            "upload",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "<object-name> -> roboflow/<project-name>.",
        mono=mono,
    )


help_functions = {
    "create_project": help_create_project,
    "download": help_download,
    "status": help_status,
    "upload": help_upload,
}
