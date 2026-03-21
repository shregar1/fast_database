# Changelog

All notable changes to **fastmvc-db-models** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Mixins:** `TimestampMixin`, `UUIDPrimaryKeyMixin`, `SoftDeleteMixin` (`mixins.py`).
- **Soft-delete helpers:** `where_not_deleted`, `select_active`, `mark_soft_deleted`, `restore_soft_deleted`, `filter_active` (`soft_delete.py`).
- **README:** Alembic autogenerate notes and example `env.py` fragment.
- Tooling aligned with the FastMVC monorepo (`Makefile`, pre-commit, Ruff, etc.).

