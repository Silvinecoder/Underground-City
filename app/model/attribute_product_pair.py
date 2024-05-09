import uuid
from sqlalchemy import Column, ForeignKey, UUID
from sqlalchemy.orm import relationship
from app.assistant.model_helper import Base


class AttributeProductPair(Base):
    """Class representing the association between products and shops."""

    __tablename__ = 'attribute_product_pair'
    attribute_product_pair_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    product_uuid = Column(UUID(as_uuid=True), ForeignKey('product.product_uuid'), nullable=False)
    attribute_uuid = Column(UUID(as_uuid=True), ForeignKey('attribute.attribute_uuid'), nullable=False)
    
    product = relationship('Product')
    attribute = relationship('Attribute')

    # Checking if attribute-product pair exists in the database, if not, create it
    @classmethod
    def get_or_create(cls, session, product, attribute):
        attribute_product_pair = session.query(AttributeProductPair).filter_by(product_uuid=product.product_uuid, attribute_uuid=attribute.attribute_uuid).first()
        if not attribute_product_pair:
            attribute_product_pair = AttributeProductPair(product=product, attribute=attribute)
            session.add(attribute_product_pair)
        return attribute_product_pair
