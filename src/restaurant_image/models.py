from src.database import metadata
from sqlalchemy import Table, Column, DateTime, func, text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


restaurant_image = Table(
    "restaurant_image",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("restaurant_id", ForeignKey("restaurant.id"), nullable=False),
    Column("image_id", ForeignKey("image.id"), nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
