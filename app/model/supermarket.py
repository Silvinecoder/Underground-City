import uuid
from sqlalchemy import Column, String, UUID

from app.assistant.model_helper import Base


class Supermarket(Base):
    """Class representing the 'supermarket' table in the database."""

    __tablename__ = 'supermarket'
    supermarket_uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    supermarket_name = Column(String(255), nullable=False)
    supermarket_country = Column(String(255), nullable=False)
    
    # Checking if supermarket exists in the database, if not, create it
    @classmethod
    def get_or_create(cls, session, supermarket_name, country):
        supermarket = session.query(Supermarket).filter_by(supermarket_name=supermarket_name).first()
        if not supermarket:
            supermarket = Supermarket(supermarket_name=supermarket_name, supermarket_country=country)
            session.add(supermarket)
        return supermarket