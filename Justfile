set shell := ["bash", "-uc"]

default:
    @just --list

test *args:
    uvx --with tox-uv tox -e py -- {{ args }}

test-all *args:
    TOX_SKIP_ENV='linting|typing' uvx --with tox-uv tox -- {{ args }}

lint:
    uvx --with tox-uv tox -e linting,typing

format:
    uv run --group lint ruff format
    uv run --group lint ruff check --fix
    uv run --group lint validate-pyproject pyproject.toml

build:
    uv build
