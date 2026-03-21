"""
fastmvc_db_models
==================

Shared SQLAlchemy ORM models intended to be reused across multiple apps.

The canonical declarative `Base` is exposed here for convenience:
`from fastmvc_db_models import Base`.

Mixins and soft-delete helpers::

    from fastmvc_db_models import Base, TimestampMixin, SoftDeleteMixin
    from fastmvc_db_models.soft_delete import select_active, mark_soft_deleted
"""

from fastmvc_db_models.models import Base
from fastmvc_db_models.mixins import SoftDeleteMixin, TimestampMixin, UUIDPrimaryKeyMixin
from fastmvc_db_models.soft_delete import (
    filter_active,
    mark_soft_deleted,
    restore_soft_deleted,
    select_active,
    where_not_deleted,
)

__all__ = [
    "Base",
    "TimestampMixin",
    "UUIDPrimaryKeyMixin",
    "SoftDeleteMixin",
    "where_not_deleted",
    "select_active",
    "mark_soft_deleted",
    "restore_soft_deleted",
    "filter_active",
]
