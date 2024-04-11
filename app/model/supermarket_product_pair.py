import uuid
from sqlalchemy import Column, ForeignKey, UUID
from sqlalchemy.orm import relationship
from app.assistant.model_helper import Base

from app.model.product import Product
from app.model.supermarket import Supermarket

class SupermarketProductPair(Base):
    """Class representing the association between products and shops."""

    __tablename__ = 'supermarket_product_pair'
    supermarket_product_pair_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    product_uuid = Column(UUID(as_uuid=True), ForeignKey('product.product_uuid'), nullable=False)
    supermarket_uuid = Column(UUID(as_uuid=True), ForeignKey('supermarket.supermarket_uuid'), nullable=False)
    
    products = relationship(Product, back_populates="supermarket_product_pair")
    supermarkets = relationship(Supermarket, back_populates="supermarket_product_pair")
