from typing import List

from blue_options.terminal import show_usage, xtra


def help_fetch(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,install,", mono=mono),
            "lat=<lat>,lon=<lon>",
            xtra(",upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "@gearth",
            "fetch",
            f"[{options}]",
            "[-|<object-name>]",
        ],
        "fetch from google earth.",
        mono=mono,
    )


help_functions = {
    "fetch": help_fetch,
}
