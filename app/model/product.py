import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy import ForeignKey

from app.assistant.model_helper import Base

class Product(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'product'
    product_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    product_name = Column(String(255), nullable=False)
    product_image = Column(String(255), nullable=True)

    product_category_uuid = Column(UUID(as_uuid=True), ForeignKey('category.category_uuid'))
    product_attribute_uuid = Column(UUID(as_uuid=True), ForeignKey('attribute.attribute_uuid'))

    # Checking if product exists in the database, if not, create it
    @classmethod
    def get_or_create(cls, session, product_name, product_image, product_category_uuid, product_attribute_uuid):
        product = session.query(Product).filter_by(product_name=product_name).first()
        if not product:
            product = Product(product_name=product_name, product_image=product_image, product_category_uuid=product_category_uuid, product_attribute_uuid=product_attribute_uuid)
            session.add(product)
        return product