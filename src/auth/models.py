from src.database import metadata
from sqlalchemy import Table, Column, DateTime, func, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID, TEXT


refresh_token = Table(
    "refresh_token",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("user_id", ForeignKey("user.id", ondelete="CASCADE"), nullable=False),
    Column("refresh_token", TEXT, nullable=False),
    Column("expired_at", DateTime, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
