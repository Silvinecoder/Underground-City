'''Products module for the database'''

from sqlalchemy import Column, String, Text, Integer, Binary
from db.model_helper import Base


class Products(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'product'
    uuid = Column(Integer, primary_key=True)
    name = Column(Text(50), nullable=False)
    ingredients = Column(Text(150), nullable=False)
    dietary_info = Column(Text(150), nullable=False)
    image = Column(Binary, nullable=False)
    # need to figure out if I want to include the price
    supermarket = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)


