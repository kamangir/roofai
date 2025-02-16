from typing import List

from blue_options.terminal import show_usage, xtra

from roofai.roboflow.project import list_of_project_types


def project_creation_args(
    mono: bool,
    cascade: bool = False,
):
    return [
        "[--name <name>]",
        "[--description <description>]",
    ] + (
        []
        if cascade
        else [
            "[--type <type>]",
            xtra("[--license <MIT>]", mono=mono),
        ]
    )


def help_create_project(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("-", mono=mono)

    args = project_creation_args(mono=mono)

    return show_usage(
        [
            "@roboflow",
            "create_project",
            f"[{options}]",
        ]
        + args,
        "create a roboflow project.",
        {"type: {}".format(" | ".join(list_of_project_types)): {}},
        mono=mono,
    )


help_functions = {
    "create_project": help_create_project,
}
