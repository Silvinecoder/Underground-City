import pytest
from app.db.db_connection import refresh_session
from app.assistant.model_helper import from_json
from app.model.category import Category
from app.model.product import Product
from app.model.attribute import Attribute

ATTRIBUTE_UUID = "71857318-0c99-4709-863b-da2c7651d879"
CATEGORY_UUID = "ccbcde92-32a7-4d2c-ab71-bd6f7d4e865e"
PRODUCT_UUID = "41396390-3609-4872-8609-86992873fe48"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    session = refresh_session()
    yield
    try:
        product = session.query(Product).filter_by(product_uuid=PRODUCT_UUID).first()
        if product:
            session.delete(product)
        
        category = session.query(Category).filter_by(category_uuid=CATEGORY_UUID).first()
        if category:
            session.delete(category)
        
        attribute = session.query(Attribute).filter_by(attribute_uuid=ATTRIBUTE_UUID).first()
        if attribute:
            session.delete(attribute)

        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def test__product__save_and_get():
    session = refresh_session()

    attribute = from_json(
        Attribute, {"attributeUuid": ATTRIBUTE_UUID, "attributeType": "test Attribute"}
    )
    session.add(attribute)
    session.commit()
    saved_attribute = session.query(Attribute).filter_by(attribute_uuid=ATTRIBUTE_UUID).one()


    category = from_json(
        Category, {"categoryUuid": CATEGORY_UUID, "categoryName": "test Category"}
    )
    session.add(category)
    session.commit()
    saved_category = session.query(Category).filter_by(category_uuid=CATEGORY_UUID).one()

    product = from_json(
        Product,
        {
            "productUuid": PRODUCT_UUID,
            "productName": "test Product",
            "productImage": "test_image.jpg",
            "productPrice": "£1,21",
            "productCategoryUuid": CATEGORY_UUID,
            "productAttributeUuid": ATTRIBUTE_UUID
        },
    )
    session.add(product)
    session.commit()

    saved_product = session.query(Product).filter_by(product_uuid=PRODUCT_UUID).one()

    assert str(saved_product.product_uuid) == PRODUCT_UUID
    assert saved_product.product_name == "test Product"
    assert saved_product.product_image == "test_image.jpg"
    assert saved_product.product_price == "£1,21"
    assert str(saved_category.category_uuid) == CATEGORY_UUID
    assert str(saved_attribute.attribute_uuid) == ATTRIBUTE_UUID
