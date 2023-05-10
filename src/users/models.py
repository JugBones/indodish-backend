from src.database import Base
from sqlalchemy import Column, DateTime, func, text
from sqlalchemy.dialects.postgresql import UUID, TEXT, BYTEA


class User(Base):
    __tablename__ = "user"

    id = Column(
        "id",
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
    )

    first_name = Column("first_name", TEXT, nullable=False)

    last_name = Column("last_name", TEXT, nullable=False)

    email = Column("email", TEXT, nullable=False, unique=True)

    hashed_password = Column("hashed_password", BYTEA, nullable=False)

    phone_number = Column("phone_number", TEXT, nullable=True, unique=True)

    created_at = Column(
        "created_at", DateTime, server_default=func.now(), nullable=False
    )
    updated_at = Column("updated_at", DateTime, onupdate=func.now(), nullable=True)
