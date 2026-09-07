"""Module to test the cookiecutter template generation."""

import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

from tests.consts import PROJECT_DIR


def initialize_git_repo(repo_dir: Path):
    """Initialize a git repository in the given directory."""
    git = shutil.which("git")
    if git is None:
        raise FileNotFoundError("git executable not found")
    subprocess.run([git, "init"], cwd=repo_dir, check=True)  # noqa: S603
    subprocess.run([git, "branch", "-M", "main"], cwd=repo_dir, check=True)  # noqa: S603
    subprocess.run([git, "add", "."], cwd=repo_dir, check=True)  # noqa: S603
    commit_msg = "feat: Initial commit by pytest fixture"
    subprocess.run([git, "commit", "-m", commit_msg], cwd=repo_dir, check=True)  # noqa: S603


def generate_project(template_dict: Dict[str, str], session_id: str) -> Path:
    """
    execute: `cookiecutter <template_directory> ...`
    """
    template_dict_copy: Dict[str, str] = deepcopy(template_dict)
    cookiecutter_config = {"default_context": template_dict_copy}
    config_file = f"cookiecutter-config-{session_id}.json"
    cookiecutter_config_fpath = PROJECT_DIR / "tests" / config_file
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "template"),
        "--no-input",
        # "--default-config",
        "--config-file",
        str(cookiecutter_config_fpath),
    ]
    print("COMMAND:", " ".join(cmd))

    subprocess.run(cmd, check=True)  # noqa: S603

    project_slug = template_dict_copy["project_slug"]
    generated_repo_dir = PROJECT_DIR / "template" / project_slug
    return generated_repo_dir
