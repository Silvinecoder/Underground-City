import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship

from app.assistant.model_helper import Base


class Supermarket(Base):
    """Class representing the 'supermarket' table in the database."""

    __tablename__ = 'supermarket'
    supermarket_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    supermarket_name = Column(String(255), nullable=False)
    supermarket_country = Column(String(255), nullable=False)

    supermarket_product_pair = relationship( 'SupermarketProductPair', back_populates='supermarkets')