from dataclasses import dataclass, field
from enum import unique
from sqlalchemy import create_engine, text, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry, relationship

from twts_api.domain import Bucket, Timeserie
from twts_api.repositories import get_session
from twts_api.repositories.db_config import DbConfig


def init_db():
    mapper_registry = registry()

    bucket_table = Table(
        "bucket",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(50), unique=True),
    )

    timeserie_table = Table(
        "timeserie",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("bucket_id", Integer, ForeignKey("bucket.id")),
        Column("name", String(50), unique=True),
    )

    mapper_registry.map_imperatively(
        Bucket,
        bucket_table,
        properties={
            "_timeseries": relationship(Timeserie, backref="bucket", order_by=timeserie_table.c.id)
        },
    )

    mapper_registry.map_imperatively(Timeserie, timeserie_table)

    with get_session(DbConfig.from_env()) as session:
        mapper_registry.metadata.create_all(session.bind)
