'''Products module for the database'''

from sqlalchemy import Column, String, Integer
from config_helper.db.model_helper import Base


class Account(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'account'
    account_uuid = Column(Integer, primary_key=True)
    account_username = Column(String(50), unique=True, nullable=False)
    account_email = Column(String(50), unique=True, nullable=False)
    # Change password to be secured
    account_password = Column(String(50), nullable=False)
    account_posts = Column(String(50), nullable=False)
    account_follow = Column(Integer, nullable=False)
    account_followers = Column(Integer, nullable=False)
    account_country = Column(String(50), nullable=False)