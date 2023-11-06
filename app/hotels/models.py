from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]


class Rooms(Base):
    __tablename__ = "rooms"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]
