"""Module to test the cookiecutter template generation."""

import shutil
from pathlib import Path
from typing import Generator

import pytest

from tests.utils.project import generate_project


@pytest.fixture(name="project_dir", scope="session")
def project_dir_fixture() -> Generator[Path, None, None]:
    """Fixture to setup and teardown the project for testing."""
    # Setup: Generate the project using the cookiecutter template
    template_values = {
        "project_name": "Test Repo",
        "project_slug": "test_repo",
        "project_description": ("Test MLOps pipeline template with automated CI/CD."),
        "author_name": "John Doe",
        "author_github_handle": "JohnDoe123",
    }
    generated_repo_dir: Path = generate_project(template_dict=template_values)

    # Yield the generated project directory to the test function
    yield generated_repo_dir

    # Teardown: Remove the generated project directory after the test is done
    shutil.rmtree(path=generated_repo_dir)


def test_can_generate_project(project_dir: Path):
    """
    Test that the cookiecutter template can generate a project without errors.
    """
    msg_false = f"Generated project directory does not exist: {project_dir}"
    assert project_dir.exists(), msg_false
