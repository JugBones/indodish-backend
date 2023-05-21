from src.database import metadata
from sqlalchemy import Table, Column, DateTime, func, text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, INTEGER


cart = Table(
    "cart",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("quantity", INTEGER, nullable=False),
    Column("dish_id", ForeignKey("dish.id"), nullable=False),
    Column("user_id", ForeignKey("user.id"), nullable=False),
    Column("refresh_token_id", ForeignKey("refresh_token.id"), nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
