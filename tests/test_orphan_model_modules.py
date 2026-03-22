"""Import model modules that are not re-exported from ``fast_database.models``."""

from __future__ import annotations


def test_standalone_model_modules_import():
    """Class bodies execute so coverage includes these tables."""
    import fast_database.models.api_key  # noqa: F401
    import fast_database.models.audit  # noqa: F401
    import fast_database.models.consent  # noqa: F401
    import fast_database.models.document  # noqa: F401
