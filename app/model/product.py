import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from app.assistant.model_helper import Base
from app.model.category import Category
from app.model.attribute import Attribute

class Product(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'product'
    product_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    product_name = Column(String(255), nullable=False)
    product_image = Column(String(255), nullable=True)

    product_category_uuid = Column(UUID(as_uuid=True), ForeignKey('category.category_uuid'))
    product_attribute_uuid = Column(UUID(as_uuid=True), ForeignKey('attribute.attribute_uuid'))

    product_category = relationship(Category, back_populates='products')
    product_attribute = relationship(Attribute, back_populates='products')
    supermarket_product_pair = relationship( 'SupermarketProductPair', back_populates='products')