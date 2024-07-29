import uuid
from sqlalchemy import Column, ForeignKey, UUID
from sqlalchemy.orm import relationship
from app.assistant.model_helper import Base

from app.model.category import Category


class SupermarketCategoryPair(Base):
    """Class representing the association between categories and shops."""

    __tablename__ = 'supermarket_category_pair'
    supermarket_category_pair_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    category_uuid = Column(UUID(as_uuid=True), ForeignKey('category.category_uuid'), nullable=False)
    supermarket_uuid = Column(UUID(as_uuid=True), ForeignKey('supermarket.supermarket_uuid'), nullable=False)
    
    category = relationship(Category)
    supermarket = relationship('Supermarket')

    # Checking if supermarket-category pair exists in the database, if not, create it
    @classmethod
    def get_or_create(cls, session, category, supermarket):
        supermarket_category_pair = session.query(SupermarketCategoryPair).filter_by(category_uuid=category.category_uuid, supermarket_uuid=supermarket.supermarket_uuid).first()
        if not supermarket_category_pair:
            supermarket_category_pair = SupermarketCategoryPair(category=category, supermarket=supermarket)
            session.add(supermarket_category_pair)
        return supermarket_category_pair