import uuid

from sqlalchemy import Column, String, UUID
from app.assistant.model_helper import Base

class Product(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'product'
    product_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=True)
    supermarket = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)