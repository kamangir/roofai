import pytest

from blue_options import string

from roofai.roboflow.project import create_project


@pytest.mark.skip(reason="no deletion API, skipped.")
def test_roboflow_create_project():
    assert create_project(
        project_name=f"test-roboflow-project-{string.timestamp()}",
        project_description="created-by-pytest",
    )
