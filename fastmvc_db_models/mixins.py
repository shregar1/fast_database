"""
Reusable SQLAlchemy declarative mixins (timestamps, UUID PK, soft-delete columns).

Use with the package :class:`fastmvc_db_models.models.Base`::

    from fastmvc_db_models import Base
    from fastmvc_db_models.mixins import TimestampMixin, UUIDPrimaryKeyMixin

    class Item(Base, UUIDPrimaryKeyMixin, TimestampMixin):
        __tablename__ = "items"
        name = Column(String(255), nullable=False)

**Mixin order:** put ``Base`` first, then mixins, then your columns.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Uuid


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class TimestampMixin:
    """``created_at`` / ``updated_at`` with UTC-aware datetimes."""

    __abstract__ = True

    created_at = Column(DateTime(timezone=True), nullable=False, default=_utc_now)
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=_utc_now)


class UUIDPrimaryKeyMixin:
    """Primary key ``id`` as UUID (SQLAlchemy :class:`Uuid` type)."""

    __abstract__ = True

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)


class SoftDeleteMixin:
    """
    ``is_deleted`` flag and optional ``deleted_at`` for soft-delete rows.

    Existing models (e.g. :class:`~fastmvc_db_models.models.user.User`) may define
    only ``is_deleted``; new tables can use this mixin for both columns and use
    helpers in :mod:`fastmvc_db_models.soft_delete`.
    """

    __abstract__ = True

    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
