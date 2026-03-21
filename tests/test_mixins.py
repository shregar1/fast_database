"""Mixins and soft-delete helpers with an in-memory SQLite schema."""

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import Session, declarative_base

from fastmvc_db_models.mixins import SoftDeleteMixin, TimestampMixin, UUIDPrimaryKeyMixin
from fastmvc_db_models.soft_delete import (
    mark_soft_deleted,
    restore_soft_deleted,
    select_active,
    where_not_deleted,
)

_Base = declarative_base()


class _Example(_Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "example_mixin_rows"
    name = Column(String(80), nullable=False)


def test_create_roundtrip_and_soft_delete():
    engine = create_engine("sqlite:///:memory:")
    _Base.metadata.create_all(engine, tables=[_Example.__table__])

    with Session(engine) as session:
        row = _Example(name="a")
        session.add(row)
        session.commit()
        rid = row.id
        assert row.is_deleted is False
        assert row.created_at is not None

        mark_soft_deleted(row)
        session.commit()

        assert row.is_deleted is True
        assert row.deleted_at is not None

        restore_soft_deleted(row)
        session.commit()
        assert row.is_deleted is False

    with Session(engine) as session:
        r2 = session.get(_Example, rid)
        assert r2 is not None
        assert r2.name == "a"


def test_select_active_where():
    engine = create_engine("sqlite:///:memory:")
    _Base.metadata.create_all(engine, tables=[_Example.__table__])

    with Session(engine) as session:
        session.add_all([_Example(name="x"), _Example(name="y")])
        session.commit()
        rows = list(session.scalars(select_active(_Example)).all())
        assert len(rows) == 2

        mark_soft_deleted(rows[0])
        session.commit()

        active = list(session.scalars(select_active(_Example)).all())
        assert len(active) == 1
        assert active[0].name == "y"

    where_not_deleted(_Example)  # expression builds
