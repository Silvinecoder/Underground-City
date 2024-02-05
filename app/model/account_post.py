'''Products module for the database'''

from sqlalchemy import Column, String, Integer, Date
from db.model_helper import Base

from model.account import Account


class Post(Base):
    """Class representing the 'products' table in the database."""

    __tablename__ = 'account_post'
    post_uuid = Column(Integer, primary_key=True)
    account_uuid = Column(Integer, primary_key=True)
    post_image = Column(String(50), nullable=False)
    post_date = Column(Date, nullable=False)
    post_caption = Column(String(50), nullable=False)
    post_likes = Column(String(50), nullable=False)
    post_dislikes = Column(String(50), nullable=False)
    post_comments = Column(String(50), nullable=False)