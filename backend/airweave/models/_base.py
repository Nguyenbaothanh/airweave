"""Base models for the application."""

import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all models."""

    id = Column(UUID, primary_key=True, default=uuid.uuid4, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )


class OrganizationBase(Base):
    """Base class for organization-related tables."""

    __abstract__ = True

    @declared_attr
    def organization_id(cls):
        """Organization ID column."""
        return Column(UUID, ForeignKey("organization.id"), nullable=False)


class UserMixin:
    """Mixin for adding user tracking columns to a model."""

    @declared_attr
    def created_by_email(cls):
        return Column(String, ForeignKey("user.email"), nullable=False)

    @declared_attr
    def modified_by_email(cls):
        return Column(String, ForeignKey("user.email"), nullable=False)
