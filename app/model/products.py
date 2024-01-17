'''Products module for the database'''

from sqlalchemy import Column, String, JSON, Integer
from db.model_helper import Base


class Products(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(50), nullable=False)
    product_description = Column(String(50), nullable=False)
    product_label = Column(String(50), nullable=False)
    product_ingredients = Column(String(50), nullable=False)
    nutrition_data = Column(JSON)
    # need to figure out if I want to include the price
    product_location = Column(String(50), nullable=False)