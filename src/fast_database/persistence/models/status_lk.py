"""Status Lookup Model.

SQLAlchemy ORM model for generic status codes (e.g. draft, paid, cancelled).
Referenced by invoice.status_id and other entities. Code is unique and used
in business logic.

Uses LookupModelMixin for standard lookup table schema:
- id, urn, code, description, created_at, updated_at
- to_dict() serialization method

Usage:
    >>> from fast_database.persistence.models.status_lk import StatusLk
    >>> # Shared across invoices and other status-carrying entities
"""

from fast_database.core.constants.table import Table
from fast_database.core.mixins import LookupModelMixin
from fast_database.persistence.models import Base


class StatusLk(Base, LookupModelMixin):
    """Lookup: generic status (e.g. draft, paid, cancelled).

    Attributes (from LookupModelMixin):
        id: Primary key.
        urn: Unique Resource Name.
        code: Unique status code.
        description: Human-readable label.
        created_at, updated_at: Timestamps.
    """

    __tablename__ = Table.STATUS_LK
