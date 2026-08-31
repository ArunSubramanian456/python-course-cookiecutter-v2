"""Module for testing the Makefile"""

import pytest


@pytest.fixture(scope="session")
def project():
    """Fixture to setup and teardown the project for testing."""
    print("Setup")
    yield 1
    print("Teardown")


def test_linting_passes(project_to_test):
    """Test that linting passes."""
    print(project_to_test)
    assert False


def test_tests_passes():
    """Test that tests pass."""


def test_install_passes():
    """Test that installation passes."""
