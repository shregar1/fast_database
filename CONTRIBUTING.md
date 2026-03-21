# Contributing to fast-db-models

Thank you for your interest in contributing.

## Monorepo layout

This package usually lives inside the **FastMVC** monorepo. From the repo root, install in editable mode:

```bash
cd fast_db_models
pip install -e ".[dev]" || pip install -e .
pip install -r requirements.txt
pre-commit install
```

Standalone clone (if this package is its own git remote):

```bash
git clone https://github.com/shregar1/fast-db-models.git
cd fast-db-models
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -e ".[dev]" || pip install -e .
pip install -r requirements.txt
pre-commit install
```

Default clone URL (set `[project.urls] Homepage` in `pyproject.toml` if different): `https://github.com/shregar1/fast-db-models.git`.

To copy EditorConfig, pre-commit config, and other shared files from `fast_middleware/` into every package:

```bash
# from monorepo root
python3 scripts/sync_package_tooling.py
```

## Test coverage

Many FastMVC libraries enforce **≥95% line coverage** via `pytest-cov` (`fail_under` in `pyproject.toml`). From this package directory:

```bash
python3 -m pytest tests/ -q --cov=src --cov-fail-under=95
```

(`fast_db_models` may use `--cov=fast_db_models`; `fast_dashboards` often uses `--cov=src/fast_dashboards` — see that package’s `pyproject.toml`.)

Overview: [../docs/COVERAGE.md](../docs/COVERAGE.md).

## Quality checks

```bash
make test
make lint
make format
```

See `Makefile` for all targets.

## Commits

Use clear commit messages (e.g. conventional commits: `feat:`, `fix:`, `docs:`).

Pull requests against `main` are welcome.
