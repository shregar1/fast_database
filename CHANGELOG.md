# Changelog

All notable changes to **fastmvc-db-models** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Mixins:** `OrganizationScopedMixin`, `TenantIdMixin`, `OptimisticLockMixin`, `AuditActorMixin` (plus `TimestampMixin`, `UUIDPrimaryKeyMixin`, `SoftDeleteMixin`).
- **Optimistic locking helpers:** `assert_version_matches`, `expected_version`, `StaleVersionError` (`optimistic_lock.py`).
- **factory_boy example:** `PlanFactory` in `fastmvc_db_models.factories` (optional `[dev]` extra includes `factory-boy`).
- **Soft-delete helpers:** `where_not_deleted`, `select_active`, `mark_soft_deleted`, `restore_soft_deleted`, `filter_active` (`soft_delete.py`).
- **README:** Alembic notes, tenant composite-index recipe, optimistic lock / audit / factory examples.
- Tooling aligned with the FastMVC monorepo (`Makefile`, pre-commit, Ruff, etc.).

