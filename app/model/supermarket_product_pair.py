import uuid
from sqlalchemy import Column, ForeignKey, UUID
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import relationship
from app.assistant.model_helper import Base

from app.model.product import Product
from app.model.supermarket import Supermarket

class SupermarketProductPair(Base):  # pragma: integration
    """Class representing the association between products and shops."""

    __tablename__ = 'supermarket_product_pair'
    supermarket_product_pair_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    product_uuid = Column(UUID(as_uuid=True), ForeignKey('product.product_uuid'), nullable=False)
    supermarket_uuid = Column(UUID(as_uuid=True), ForeignKey('supermarket.supermarket_uuid'), nullable=False)
    
    product = relationship(Product)
    supermarket = relationship(Supermarket)

    # Checking if supermarket-product pair exists in the database, if not, create it
    @classmethod
    def get_or_create(cls, session, product, supermarket):  # pragma: integration
        try:
            supermarket_product_pair = session.query(SupermarketProductPair).filter_by(product_uuid=product.product_uuid, supermarket_uuid=supermarket.supermarket_uuid).first()
        except NoResultFound:
            supermarket_product_pair = SupermarketProductPair(product=product, supermarket=supermarket)
            session.add(supermarket_product_pair)
        return supermarket_product_pair
