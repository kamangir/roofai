from blue_options import string

from roofai.roboflow.create import create_project


def test_roboflow_create_project():
    assert create_project(
        project_name="roofai-pytest-roboflow-create-project",
        project_description="created-by-pytest",
    )
