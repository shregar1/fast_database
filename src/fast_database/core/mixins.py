"""
Core Mixins for Fast Database Models.

Provides reusable mixins for common model patterns like lookup tables,
timestamp handling, and serialization.

This module follows DRY principles to eliminate code duplication across
model definitions.

Example:
    >>> from fast_database.core.mixins import LookupModelMixin
    >>> from fast_database.persistence.models import Base
    >>> 
    >>> class StatusLk(Base, LookupModelMixin):
    ...     __tablename__ = "status_lk"
    ...     # id, urn, code, description, created_at, updated_at are provided
    ...     # to_dict() method is provided
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from sqlalchemy import BigInteger, Column, DateTime, String


class LookupModelMixin:
    """
    Mixin for lookup table models with standard schema.
    
    Provides common lookup table columns:
    - id: Primary key (BigInteger, autoincrement)
    - urn: Unique Resource Name (String 128, unique, indexed)
    - code: Unique code (String 64, unique, indexed)
    - description: Human-readable label (String 255)
    - created_at: Timestamp (DateTime, not null, default utcnow)
    - updated_at: Timestamp (DateTime, nullable, onupdate utcnow)
    
    Also provides a standard to_dict() serialization method.
    
    Attributes:
        id (int): Primary key
        urn (str): Unique Resource Name
        code (str): Unique code for business logic
        description (str): Human-readable description
        created_at (datetime): Creation timestamp
        updated_at (datetime): Last update timestamp
    
    Example:
        >>> from fast_database.persistence.models import Base
        >>> from fast_database.core.mixins import LookupModelMixin
        >>> from fast_database.core.constants.table import Table
        >>> 
        >>> class StatusLk(Base, LookupModelMixin):
        ...     __tablename__ = Table.STATUS_LK
        ...     # All columns and methods provided by mixin
        ...     pass
        >>> 
        >>> status = StatusLk(urn="urn:status:active", code="active", description="Active")
        >>> status.to_dict()
        {'urn': 'urn:status:active', 'code': 'active', 'description': 'Active', 
         'created_at': '2024-01-01T00:00:00', 'updated_at': None}
    """

    # Primary key
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    
    # Unique identifiers
    urn = Column(String(128), nullable=False, unique=True, index=True)
    code = Column(String(64), nullable=False, unique=True, index=True)
    
    # Description
    description = Column(String(255), nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=datetime.utcnow)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the lookup record to a dictionary.
        
        Returns:
            Dictionary with urn, code, description, created_at, updated_at.
            Datetimes are ISO-formatted strings.
            
        Example:
            >>> status = StatusLk(urn="urn:status:active", code="active", 
            ...                   description="Active status")
            >>> status.to_dict()
            {'urn': 'urn:status:active', 'code': 'active', 
             'description': 'Active status', 'created_at': '2024-01-01T00:00:00', 
             'updated_at': None}
        """
        return {
            "urn": self.urn,
            "code": self.code,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class TimestampMixin:
    """
    Mixin for models requiring created_at and updated_at timestamps.
    
    Provides:
    - created_at: Timestamp (DateTime, not null, default utcnow)
    - updated_at: Timestamp (DateTime, nullable, onupdate utcnow)
    
    Example:
        >>> from fast_database.persistence.models import Base
        >>> from fast_database.core.mixins import TimestampMixin
        >>> 
        >>> class MyModel(Base, TimestampMixin):
        ...     __tablename__ = "my_model"
        ...     # created_at and updated_at columns provided
    """

    created_at = Column(
        DateTime(timezone=True), 
        nullable=False, 
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime(timezone=True), 
        nullable=True, 
        onupdate=datetime.utcnow
    )


class URNMixin:
    """
    Mixin for models requiring a URN (Unique Resource Name).
    
    Provides:
    - urn: Unique Resource Name (String 128, unique, indexed)
    
    Example:
        >>> from fast_database.persistence.models import Base
        >>> from fast_database.core.mixins import URNMixin
        >>> 
        >>> class MyModel(Base, URNMixin):
        ...     __tablename__ = "my_model"
        ...     # urn column provided
    """

    urn = Column(String(128), nullable=False, unique=True, index=True)
