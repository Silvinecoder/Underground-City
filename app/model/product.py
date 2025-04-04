import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm.exc import NoResultFound

from app.assistant.model_helper import Base


class Product(Base):  # pragma: integration
    """Class representing the 'products' table in the database."""

    __tablename__ = 'product'
    product_uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        nullable=False,
    )
    product_name = Column(String(255), nullable=False)
    product_image = Column(String(255), nullable=True)
    product_price = Column(String(255), nullable=True)

    product_category_uuid = Column(UUID(as_uuid=True), ForeignKey('category.category_uuid'))
    product_attribute_uuid = Column(UUID(as_uuid=True), ForeignKey('attribute.attribute_uuid'))

    # Checking if product exists in the database, if not, create it
    @classmethod
    def get_or_create(
        cls,
        session,
        product_name,
        product_image,
        product_price,
        product_category_uuid,
        product_attribute_uuid,
    ):  # pragma: integration
        try:
            product = session.query(Product).filter_by(product_name=product_name).first()
        except NoResultFound:
            product = Product(
                product_name=product_name,
                product_image=product_image,
                product_price=product_price,
                product_category_uuid=product_category_uuid,
                product_attribute_uuid=product_attribute_uuid,
            )
            session.add(product)
        return product
