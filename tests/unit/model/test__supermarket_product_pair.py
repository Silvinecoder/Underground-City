from app.model.supermarket_product_pair import SupermarketProductPair
from app.assistant.model_helper import from_json


def test__product__from_json():
    data = {
        "supermarketProductPairUuid": "123e4567-e89",
        "productUuid": "123e4567-e89777-123e4567-e89",
        "supermarketUuid": "123e4567-e89-123e4567-e89788",
    }
    supermarket_product_pair = from_json(SupermarketProductPair, data)
    assert supermarket_product_pair.supermarket_product_pair_uuid == "123e4567-e89"
    assert supermarket_product_pair.product_uuid == "123e4567-e89777-123e4567-e89"
    assert supermarket_product_pair.supermarket_uuid == "123e4567-e89-123e4567-e89788"

def test__product__from_json_missing_field():
    data = {
        "supermarketProductPairUuid": "123e4567-e89",
        "productUuid": "123e4567-e89777-123e4567-e89",
    }
    supermarket_product_pair = from_json(SupermarketProductPair, data)
    assert supermarket_product_pair.supermarket_product_pair_uuid == "123e4567-e89"
    assert supermarket_product_pair.product_uuid == "123e4567-e89777-123e4567-e89"

def test__product__from_json_invalid_field():
    data = {
        "supermarketProductPairUuid": "123e4567-e89",
        "productUuid": "123e4567-e89777-123e4567-e89",
        "supermarketUuid": "123e4567-e89-123e4567-e89788",
        "invalidField": "test"
    }
    supermarket_product_pair = from_json(SupermarketProductPair, data)
    assert supermarket_product_pair.supermarket_product_pair_uuid == "123e4567-e89"
    assert supermarket_product_pair.product_uuid == "123e4567-e89777-123e4567-e89"
    assert supermarket_product_pair.supermarket_uuid == "123e4567-e89-123e4567-e89788"
    assert not hasattr(supermarket_product_pair, 'invalid_field')
