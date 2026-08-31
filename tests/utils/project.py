"""Module to test the cookiecutter template generation."""

import json
import subprocess
from copy import deepcopy
from typing import Dict

from tests.consts import PROJECT_DIR


def generate_project(template_dict: Dict[str, str]):
    """
    execute: `cookiecutter <template_directory> ...`
    """
    template_dict_copy: Dict[str, str] = deepcopy(template_dict)
    cookiecutter_config = {"default_context": template_dict_copy}
    config_file = "cookiecutter-test-config.json"
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
