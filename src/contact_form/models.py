from sqlalchemy import Table, Column, text
from sqlalchemy.dialects.postgresql import UUID, TEXT
from src.database import metadata

contact_form = Table(
    "contact_form",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("name", TEXT, nullable=False),
    Column("email", TEXT, nullable=False),
    Column("phone_number", TEXT, nullable=False),
    Column("message", TEXT, nullable=False),
)
