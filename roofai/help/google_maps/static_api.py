from typing import List

from blue_options.terminal import show_usage, xtra


def help_get_static_image(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = [
        "[--lat <lat>]",
        "[--lon <lon>]",
        "[--filename <filename>]",
        "[--zoom <20>]",
        "[--maptype satellite]",
        "[--size 640x640]",
    ]

    return show_usage(
        [
            "@gmaps",
            "get_static_image",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "get Google Maps Static Image.",
        {
            "https://developers.google.com/maps/documentation/maps-static/start": [],
        },
        mono=mono,
    )
