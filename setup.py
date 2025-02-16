from roofai import NAME, VERSION, DESCRIPTION, REPO_NAME
from blueness.pypi import setup


setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.dataset",
        f"{NAME}.dataset.ingest",
        f"{NAME}.google_maps",
        f"{NAME}.google_maps.api",
        f"{NAME}.google_maps.semseg",
        f"{NAME}.help",
        f"{NAME}.help.google_maps",
        f"{NAME}.roboflow",
        f"{NAME}.semseg",
        f"{NAME}.tests",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
        ],
    },
)
