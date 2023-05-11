from src.database import metadata
from sqlalchemy import Table, Column, DateTime, func, text
from sqlalchemy.dialects.postgresql import UUID, TEXT, BYTEA


user = Table(
    "user",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("first_name", TEXT, nullable=False),
    Column("last_name", TEXT, nullable=False),
    Column("email", TEXT, nullable=False, unique=True),
    Column("hashed_password", BYTEA, nullable=False),
    Column("phone_number", TEXT, nullable=True, unique=True),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
