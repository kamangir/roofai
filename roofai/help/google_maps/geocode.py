from typing import List

from blue_options.terminal import show_usage, xtra


def help_geocode(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("-", mono=mono)

    args = [
        "[--address <address>]",
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@gmaps",
            "geocode",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "geocode <address>.",
        mono=mono,
    )
