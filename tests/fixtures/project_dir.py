"""Module to test the cookiecutter template generation."""

import shutil
import subprocess
from pathlib import Path
from typing import Generator
from uuid import uuid4

import pytest

from tests.utils.project import generate_project, initialize_git_repo


def generate_test_session_id() -> str:
    """Generate a unique test session ID."""
    test_session_id = str(uuid4())[:6]
    return test_session_id


@pytest.fixture(name="project_dir", scope="session")
def project_dir_fixture() -> Generator[Path, None, None]:
    """Fixture to setup and teardown the project for testing."""
    # Setup: Generate the project using the cookiecutter template
    test_session_id: str = generate_test_session_id()
    template_values = {
        "project_name": f"Test Repo {test_session_id}",
        "project_slug": f"test_repo_{test_session_id}",
        "project_description": ("Test MLOps pipeline template with automated CI/CD."),
        "author_name": "John Doe",
        "author_github_handle": "JohnDoe123",
    }
    generated_repo_dir: Path = generate_project(template_dict=template_values, session_id=test_session_id)
    try:
        initialize_git_repo(repo_dir=generated_repo_dir)
        make = shutil.which("make")
        if make is None:
            raise FileNotFoundError("make executable not found")
        subprocess.run([make, "lint-ci"], cwd=generated_repo_dir, check=False)  # noqa: S603
        # Yield the generated project directory to the test function
        yield generated_repo_dir
    except Exception as e:
        # If an exception occurs during setup, print the error and re-raise it
        print(f"Error during project setup: {e}")
        raise
    finally:
        # Teardown: Remove the generated project directory after the test is done
        shutil.rmtree(path=generated_repo_dir)
        # Remove the cookiecutter config file after the test is done
        config_file = f"cookiecutter-config-{test_session_id}.json"
        cookiecutter_config_fpath = Path(__file__).parent.parent / config_file
        if cookiecutter_config_fpath.exists():
            cookiecutter_config_fpath.unlink(missing_ok=True)
