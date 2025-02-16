from typing import List

from blue_options.terminal import show_usage, xtra

from roofai.roboflow.project import list_of_project_types


def help_create_project(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("-", mono=mono)

    args = [
        "[--name <name>]",
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
        {"type: {}".format(" | ".join(list_of_project_types)): {}},
        mono=mono,
    )


help_functions = {
    "create_project": help_create_project,
}
