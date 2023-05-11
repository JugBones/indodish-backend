from src.database import Base
from sqlalchemy import Column, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TEXT


class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id = Column("id", UUID(as_uuid=True), primary_key=True)

    user_id = Column(
        "user_id", ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )

    refresh_token = Column("refresh_token", TEXT, nullable=False)

    expires_at = Column("expires_at", DateTime, nullable=False)

    created_at = Column(
        "created_at", DateTime, server_default=func.now(), nullable=False
    )

    updated_at = Column("updated_at", DateTime, onupdate=func.now(), nullable=True)
