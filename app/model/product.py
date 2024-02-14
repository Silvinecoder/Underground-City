'''Products module for the database'''

from sqlalchemy import Column, String, UUID
from app.db.model_helper import Base

class Product(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'product'
    
    product_uuid = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(50), nullable=False)
    # image = Column(Binary, nullable=False)
    supermarket = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)


