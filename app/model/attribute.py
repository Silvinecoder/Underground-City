import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship

from app.assistant.model_helper import Base

class Attribute(Base):
    """Class representing the 'product attribute' table in the database."""

    __tablename__ = 'attribute'
    attribute_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    attribute_type = Column(String(255), nullable=False)

    products = relationship('Product', back_populates='product_attribute')
