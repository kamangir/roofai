from typing import List

from blue_options.terminal import show_usage, xtra


def help_fetch(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,install,", mono=mono),
            "upload",
        ]
    )

    args = [
        "[--latitude=<49.279802>]",
        "[--longitude=<-123.115660>]",
        "[--screenSpaceError=<2>]",
        "[--width=<230>]",
        "[--height=<175>]",
        "[--zoom=<19>]",
    ]

    return show_usage(
        [
            "@gearth",
            "fetch",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "fetch from google earth.",
        mono=mono,
    )


help_functions = {
    "fetch": help_fetch,
}
