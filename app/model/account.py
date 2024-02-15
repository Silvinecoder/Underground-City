from sqlalchemy import Column, String, Integer, UUID
from app.assistant.model_helper import Base


class Account(Base):
    """Class representing the 'accounts' table in the database."""

    __tablename__ = 'account'
    account_uuid = Column(UUID(as_uuid=True), primary_key=True)
    account_username = Column(String(50), unique=True, nullable=False)
    account_email = Column(String(50), unique=True, nullable=False)
    # Change password to be secured
    account_password = Column(String(50), unique=True, nullable=False)
    account_posts = Column(String(50), nullable=False)
    account_follow = Column(Integer, nullable=False)
    account_followers = Column(Integer, nullable=False)
    account_country = Column(String(50), nullable=False)