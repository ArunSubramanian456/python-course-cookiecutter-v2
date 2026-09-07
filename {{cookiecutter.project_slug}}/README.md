# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Overview

This project is a Python package template for building production-ready MLOps workflows with automated testing, linting, and CI/CD support.

## Quick start

```bash
pip install {{ cookiecutter.project_slug }}
```

```python
from {{ cookiecutter.project_slug }} import ...
```

## Project structure

- `src/{{ cookiecutter.project_slug }}/` contains the package code
- `tests/` contains the automated test suite
- `Makefile` provides common development commands
- `pyproject.toml` configures packaging and tooling

## Development

```bash
# clone the repo
git clone https://github.com/{{ cookiecutter.author_github_handle }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# install the dev dependencies
make install

# run the tests
make test
```

## Contributing

Pull requests and issues are welcome. Please keep changes focused, add or update tests when needed, and run the project checks before submitting a contribution.
