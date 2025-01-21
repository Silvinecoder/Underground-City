import pytest
from app.db.db_connection import refresh_session
from app.assistant.model_helper import from_json
from app.model.supermarket import Supermarket
from app.model.product import Product
from app.model.category import Category
from app.model.attribute import Attribute
from app.model.supermarket_product_pair import SupermarketProductPair

SUPERMARKET_PRODUCT_PAIR_UUID = "41396390-3609-4872-8609-86992873fe48"
SUPERMARKET_UUID = "07c1904a-67ef-46f8-90fb-4d04e6c759c5"
CATEGORY_UUID = "ccbcde92-32a7-4d2c-ab71-bd6f7d4e865e"
ATTRIBUTE_UUID = "71857318-0c99-4709-863b-da2c7651d879"
PRODUCT_UUID = "ccbcde92-32a7-4d2c-ab71-bd6f7d4e865e"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    session = refresh_session()
    yield
    try:
        supermarket_product_pair = (
            session.query(SupermarketProductPair)
            .filter_by(supermarket_product_pair_uuid=SUPERMARKET_PRODUCT_PAIR_UUID)
            .first()
        )
        if supermarket_product_pair:
            session.delete(supermarket_product_pair)

        supermarket = (
            session.query(Supermarket)
            .filter_by(supermarket_uuid=SUPERMARKET_UUID)
            .first()
        )
        if supermarket:
            session.delete(supermarket)

        product = session.query(Product).filter_by(product_uuid=PRODUCT_UUID).first()
        if product:
            session.delete(product)

        category = (
            session.query(Category).filter_by(category_uuid=CATEGORY_UUID).first()
        )
        if category:
            session.delete(category)

        attribute = (
            session.query(Attribute).filter_by(attribute_uuid=ATTRIBUTE_UUID).first()
        )
        if attribute:
            session.delete(attribute)

        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def test__supermarket_product_pair__save_and_get():
    session = refresh_session()

    supermarket = from_json(
        Supermarket,
        {
            "supermarketUuid": SUPERMARKET_UUID,
            "supermarketName": "test Supermarket",
            "supermarketCountry": "test UK",
        },
    )
    session.add(supermarket)
    session.commit()
    saved_supermarket = (
        session.query(Supermarket).filter_by(supermarket_uuid=SUPERMARKET_UUID).one()
    )

    attribute = from_json(
        Attribute, {"attributeUuid": ATTRIBUTE_UUID, "attributeType": "test Attribute"}
    )
    session.add(attribute)
    session.commit()
    saved_attribute = (
        session.query(Attribute).filter_by(attribute_uuid=ATTRIBUTE_UUID).one()
    )

    category = from_json(
        Category, {"categoryUuid": CATEGORY_UUID, "categoryName": "test Category"}
    )
    session.add(category)
    session.commit()
    saved_category = (
        session.query(Category).filter_by(category_uuid=CATEGORY_UUID).one()
    )

    product = from_json(
        Product,
        {
            "productUuid": PRODUCT_UUID,
            "productName": "test Product",
            "productImage": "test_image.jpg",
            "productPrice": "£1.21",
            "productCategoryUuid": CATEGORY_UUID,
            "productAttributeUuid": ATTRIBUTE_UUID,
        },
    )
    session.add(product)
    session.commit()
    saved_product = session.query(Product).filter_by(product_uuid=PRODUCT_UUID).one()

    supermarket_product_pair = from_json(
        SupermarketProductPair,
        {
            "supermarketProductPairUuid": SUPERMARKET_PRODUCT_PAIR_UUID,
            "productUuid": PRODUCT_UUID,
            "supermarketUuid": SUPERMARKET_UUID,
        },
    )
    session.add(supermarket_product_pair)
    session.commit()

    saved_supermarket_product_pair = (
        session.query(SupermarketProductPair)
        .filter_by(supermarket_product_pair_uuid=SUPERMARKET_PRODUCT_PAIR_UUID)
        .one()
    )

    assert (
        str(saved_supermarket_product_pair.supermarket_product_pair_uuid)
        == SUPERMARKET_PRODUCT_PAIR_UUID
    )
    assert str(saved_product.product_uuid) == PRODUCT_UUID
    assert str(saved_category.category_uuid) == CATEGORY_UUID
    assert str(saved_attribute.attribute_uuid) == ATTRIBUTE_UUID
    assert str(saved_supermarket.supermarket_uuid) == SUPERMARKET_UUID