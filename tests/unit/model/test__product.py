from app.model.product import Product
from app.assistant.model_helper import from_json


def test__product__from_json():
    data = {
        "productUuid": "123e4567-e89",
        "productName": "test product",
        "productImage": "test_image.jpg",
        "productPrice": "£1,21",
        "productCategoryUuid": "123e4567-e89",
        "productAttributeUuid": "123e4567-e89"
    }
    product = from_json(Product, data)
    assert product.product_uuid == "123e4567-e89"
    assert product.product_name == "test product"
    assert product.product_image == "test_image.jpg"
    assert product.product_price == "£1,21"
    assert product.product_category_uuid == "123e4567-e89"
    assert product.product_attribute_uuid == "123e4567-e89"

def test__product__from_json_missing_field():
    data = {
        "productUuid": "123e4567-e89",
        "productName": "test product",
        "productImage": "test_image.jpg",
        "productPrice": "£1,21",
        "productCategoryUuid": "123e4567-e89"
    }
    product = from_json(Product, data)
    assert product.product_uuid == "123e4567-e89"
    assert product.product_name == "test product"
    assert product.product_image == "test_image.jpg"
    assert product.product_price == "£1,21"
    assert product.product_category_uuid == "123e4567-e89"
    assert product.product_attribute_uuid is None

def test__product__from_json_invalid_field():
    data = {
        "productUuid": "123e4567-e89",
        "productName": "test product",
        "productImage": "test_image.jpg",
        "productPrice": "£1,21",
        "productCategoryUuid": "123e4567-e89",
        "invalidField": "test"
    }
    product = from_json(Product, data)
    assert product.product_uuid == "123e4567-e89"
    assert product.product_name == "test product"
    assert product.product_image == "test_image.jpg"
    assert product.product_price == "£1,21"
    assert product.product_category_uuid == "123e4567-e89"
    assert not hasattr(product, 'invalid_field')
