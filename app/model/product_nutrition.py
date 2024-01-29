'''Nutrition module for the database'''

from sqlalchemy import Column, String, Integer
from config_helper.db.model_helper import Base


class Nutrition(Base):
    """Class representing the 'nutrition' table in the database."""

    __tablename__ = 'nutrition'
    nutrition_uuid = Column(Integer, primary_key=True)
    nutrition_energy = Column(Integer, nullable=False)
    nutrition_fat = Column(String(50), nullable=False)
    nutrition_of_which_saturates = Column(String(50), nullable=False)
    nutrition_carbohydrates = Column(String(50), nullable=False)
    nutrtion_of_which_sugars = Column(String(50), nullable=False)
    nutrition_protein = Column(String(50), nullable=False)
    nutrition_salt = Column(String(50), nullable=False)