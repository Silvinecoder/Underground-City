import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship

from app.assistant.model_helper import Base

class Category(Base):
    """Class representing the 'category' table in the database."""
    __tablename__ = 'category'
    category_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    category_name = Column(String(255), nullable=False)

    products = relationship('Product', back_populates='product_category')

