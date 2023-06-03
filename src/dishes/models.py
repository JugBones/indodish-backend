from src.database import metadata
from sqlalchemy import Table, Column, DateTime, func, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID, TEXT, INTEGER, ENUM, MONEY


dish = Table(
    "dish",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    ),
    Column("name", TEXT, nullable=False, unique=True),
    Column("description", TEXT, nullable=True),
    Column(
        "restaurant_id", ForeignKey("restaurant.id", ondelete="CASCADE"), nullable=False
    ),
    Column(
        "category",
        ENUM(
            "snack",
            "appetizer",
            "main_course",
            "dessert",
            "beverage",
            name="dish_category",
        ),
    ),
    Column("price", MONEY, nullable=False),
    Column("rating_sum", INTEGER, nullable=False, default=0),
    Column("number_of_voters", INTEGER, nullable=False, default=0),
    Column(
        "region",
        ENUM("jawa", "kalimantan", "papua", "sulawesi", "sumatra", name="dish_region"),
    ),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
