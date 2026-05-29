from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlalchemy import String, Float, ForeignKey, Boolean, DateTime, text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db


class Category(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
        unique=True
    )

    products: Mapped[List['Product']] = relationship(
        'Product',
        back_populates='category',
        lazy='select'
    )

    def __repr__(self):
        return f'<Category {self.name}>'


class Product(db.Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(80),
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default=text('1')
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    category_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('categories.id'),
        nullable=True
    )

    category: Mapped[Optional[Category]] = relationship(
        'Category',
        back_populates='products'
    )

    def __repr__(self):
        return f'<Product {self.name} - {self.price}>'