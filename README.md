# Python Course Cookiecutter v2

This repository is a Cookiecutter template for generating a production-ready Python project scaffold with a modern MLOps-oriented layout. It is designed to help you quickly create a new Python package with standard tooling for testing, linting, local automation, and project configuration.

## Overview

The template packages a repeatable project setup into a single source of truth. Instead of copying boilerplate by hand, you use Cookiecutter to generate a fresh repository with customizable values:

- project name
- project description
- author name
- GitHub handle

This makes it easy to start a new Python service or package while following a consistent structure and development workflow.

## Features

- Generates a Python package skeleton from a reusable template
- Includes `pyproject.toml` configuration for tooling and packaging
- Provides a `Makefile` and `run.sh` for common developer tasks
- Supplies a test suite for validating template generation
- Keeps generated projects organized with `src/`, `tests/`, and config files
- Supports rapid local setup and project bootstrapping

## Tools Used

1. **Cookiecutter**: A framework for creating project templates. It uses placeholders to generate files with project-specific values.
2. **Jinja**: A templating engine used by Cookiecutter for string substitution in files and filenames.
3. **GitHub CLI**: A command-line tool for interacting with GitHub, allowing automation of repository creation, secret setting, and other tasks.
4. **Pytest**: A testing framework for Python. The project uses an advanced pytest plugin for running tests in parallel, enhancing test efficiency.
5. **SetupTools**: A package development tool that simplifies the process of packaging and distributing Python projects.
6. **Linting Tools**: Includes `ty`, `radon`, `ruff`, `pytest`, `pytest-cov`, and `pre-commit` for ensuring code quality and consistency.
7. **Enviroment and Package Manager**: Uses `uv venv .venv` to setup the virtual environment and `uv pip install ....` to install dependencies.


## Starting a new project

This repository is not the project you develop in directly. Instead, it acts as a template that creates a new repository for you through GitHub Actions.

1. **Fork the repository to your GitHub account.**

2. **Setup a Personal Access Token:** Create a `PERSONAL_GITHUB_TOKEN` token with the following permissions and add it as a secret to the repository.

   | Permission | Access |
   |:----------:|:------:|
   | Administration | Read and write |
   | Actions | Read and write |
   | Contents | Read and write |
   | Environments | Read and write |
   | Metadata | Read-only |
   | Pull requests | Read and write |
   | Secret scanning alerts | Read and write |
   | Secrets | Read and write |
   | Variables | Read and write |
   | Workflows | Read and write |

3. **Optional: add AWS credentials as GitHub secrets** if you want the generated repository to be configured with cloud access. In GitHub, add the following repository secrets if you plan to use AWS-based deployment or infrastructure features:

   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_DEFAULT_REGION`

   These are optional for the initial project generation flow. They are used by the repository configuration step to populate the generated repository with AWS credentials.

4. Open the repository in GitHub and trigger the workflow named `Create or Update Repo`.

5. Complete the workflow form with the details for the new project, such as:

   - repository name
   - repository description
   - visibility (`public` or `private`)
   - any other optional metadata for the generated project

6. Submit the form to start the repository generation process. The workflow creates a new GitHub repository and populates it using the Cookiecutter template.

7. Review the pull request that the workflow automatically opens. This pull request contains the generated project files and configuration.

8. Approve and merge the pull request into the repository's `main` branch.

9. Once the merge is complete, clone the newly generated repository locally:

   ```bash
   git clone https://github.com/<your-github-user>/<new-repo-name>.git
   cd <new-repo-name>
   ```

10. Create a new virtual environment inside the generated project and install its dependencies:

   ```bash
   uv venv .venv
   source .venv/bin/activate
   make install
   ```

11. Run the project validation commands in the generated repository:

   ```bash
   make lint-ci
   make test
   ```

12. At this point, you are ready to begin real development in the new project and customize the code to fit your application.

This flow is designed so that the end user does not need to write any code in the template repository itself. The generation workflow handles the project setup, and the actual project work begins only after the generated repository is created and merged.

> The repo-generation workflow can still proceed without AWS secrets. The AWS credential setup is optional and mainly supports cloud integration after the project is generated. The required setup for the template flow is the GitHub token plus the workflow form inputs.

## Generated project layout

The generated project is intended to look like a clean Python package repository with a small, modern development setup. A representative final structure is:

```text

├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .vscode/
│   ├── extensions.json
│   └── settings.json
├── Makefile
├── README.md
├── pyproject.toml
├── run.sh
├── version.txt
├── src/
│   └── <project_slug>/
│       ├── __init__.py
│       └── ...
├── tests/
│   ├── conftest.py
│   ├── consts.py
│   ├── fixtures/
│   │   └── ...
│   └── unit_tests/
│       └── test_*.py
└──
```

This reflects the typical output you get from the template, including the package source directory, test suite, repository automation, and standard configuration files used for linting, formatting, and CI workflows.

## Development commands for your new project

This repository includes a small set of automation commands through the root `Makefile`:

```bash
make help
make install
make lint-ci
make test-ci
make test-wheel-locally

```

The underlying shell script in `run.sh` defines these actions and centralizes the template workflow.

## Testing

To run the repository tests:

```bash
make test
make test-ci
```

This validates the template generation flow and helps ensure the scaffold remains usable.

## Why use this template?

It is useful when you want to:

- standardize Python project setup across multiple repositories
- reduce boilerplate for new projects
- follow a consistent package layout and toolchain
- accelerate onboarding for Python and MLOps workflows

## Notes

This project is a reusable template, not a final application by itself. The real value comes from generating a project from it and then customizing the output to fit your specific domain or team workflow.
