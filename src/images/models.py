from src.database import metadata
from sqlalchemy import Table, Column, DateTime, func, text
from sqlalchemy.dialects.postgresql import UUID, TEXT, INTEGER


image = Table(
    "image",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("url", TEXT, nullable=False),
    Column("alt", TEXT, nullable=False),
    Column("width", INTEGER, nullable=False),
    Column("height", INTEGER, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
