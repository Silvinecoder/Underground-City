import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm.exc import NoResultFound

from app.assistant.model_helper import Base


class Attribute(Base):  # pragma: integration
    """Class representing the product attribute table, ex: celiac, in the database."""

    __tablename__ = 'attribute'
    attribute_uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        nullable=False,
    )
    attribute_type = Column(String(255), nullable=False)

    # Checking if attribute exists in the database, if not, create it
    @classmethod
    def get_or_create(cls, session, attribute_type):  # pragma: integration
        try:
            attribute = (
                session.query(Attribute).filter_by(attribute_type=attribute_type).first()
            )
        except NoResultFound:
            attribute = Attribute(attribute_type=attribute_type)
            session.add(attribute)
        return attribute
