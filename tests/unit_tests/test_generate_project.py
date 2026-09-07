"""Module to test the cookiecutter template generation."""

from pathlib import Path


def test_can_generate_project(project_dir: Path):
    """
    Test that the cookiecutter template can generate a project without errors.
    """
    msg_false = f"Generated project directory does not exist: {project_dir}"
    assert project_dir.exists(), msg_false
