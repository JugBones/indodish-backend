from src.database import metadata
from sqlalchemy import Table, Column, DateTime, func, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID, TEXT, INTEGER


restaurant = Table(
    "restaurant",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("name", TEXT, nullable=False, unique=True),
    Column("description", TEXT, nullable=True),
    Column("phone_number", TEXT, nullable=False, unique=True),
    Column(
        "address_id",
        ForeignKey("address.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    ),
    Column("rating_sum", INTEGER, nullable=False, default=0),
    Column("number_of_voters", INTEGER, nullable=False, default=0),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
