import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm.exc import NoResultFound

from app.assistant.model_helper import Base


class Category(Base):  # pragma: integration
    """Class representing the 'category' table in the database."""

    __tablename__ = 'category'
    category_uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        nullable=False,
    )
    category_name = Column(String(255), nullable=False)

    # Checking if category exists in the database, if not, create it, else
    @classmethod
    def get_or_create(cls, session, category_name):  # pragma: integration
        try:
            category = (
                session.query(Category).filter_by(category_name=category_name).first()
            )
        except NoResultFound:
            category = Category(category_name=category_name)
            session.add(category)
        return category
