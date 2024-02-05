'''Products module for the database'''

from sqlalchemy import Column, String, Text, Integer, Binary
from db.model_helper import Base


class Product(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'product'
    uuid = Column(Integer, primary_key=True)
    name = Column(Text(50), nullable=False)
    # image = Column(Binary, nullable=False)
    supermarket = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)


