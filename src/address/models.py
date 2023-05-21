from src.database import metadata
from sqlalchemy import Table, Column, DateTime, func, text
from sqlalchemy.dialects.postgresql import UUID, TEXT, FLOAT


address = Table(
    "address",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("description", TEXT, nullable=False),
    Column("street_address", TEXT, nullable=False),
    Column("country", TEXT, nullable=False),
    Column("city", TEXT, nullable=False),
    Column("city_district", TEXT, nullable=False),
    Column("postal_code", TEXT, nullable=False),
    Column("latitude", FLOAT, nullable=False),
    Column("longitude", FLOAT, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
