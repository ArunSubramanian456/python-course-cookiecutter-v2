"""Module for testing the Makefile"""

import shutil
import subprocess
from pathlib import Path


def test_linting_passes(project_dir: Path):
    """Test that linting passes"""
    make = shutil.which("make")
    if make is None:
        raise FileNotFoundError("make executable not found")
    subprocess.run([make, "lint-ci"], cwd=project_dir, check=True)  # noqa: S603


def test_tests_passes(project_dir: Path):
    """Test that tests passes"""
    make = shutil.which("make")
    if make is None:
        raise FileNotFoundError("make executable not found")
    subprocess.run([make, "install"], cwd=project_dir, check=True)  # noqa: S603
    subprocess.run([make, "test-wheel-locally"], cwd=project_dir, check=True)  # noqa: S603


def test_install_passes(project_dir: Path):
    """Test that installation passes"""
    make = shutil.which("make")
    if make is None:
        raise FileNotFoundError("make executable not found")
    subprocess.run([make, "install"], cwd=project_dir, check=True)  # noqa: S603
