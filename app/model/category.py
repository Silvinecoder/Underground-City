import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound

from app.assistant.model_helper import Base

class Category(Base):
    """Class representing the 'category' table in the database."""
    __tablename__ = 'category'
    category_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    category_name = Column(String(255), nullable=False)

    products = relationship('Product', back_populates='product_category')

    @classmethod
    def get_or_create(cls, session, category_name):
        try:
            # Query category by name
            category = session.query(cls).filter_by(category_name=category_name).one()
        except NoResultFound:
            # If the category doesn't exist, create a new one
            category = cls(category_name=category_name)
            session.add(category)
        return category