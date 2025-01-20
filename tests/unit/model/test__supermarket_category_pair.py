from app.model.supermarket_category_pair import SupermarketCategoryPair
from app.assistant.model_helper import from_json


def test__product__from_json():
    data = {
        "supermarketCategoryPairUuid": "123e4567-e89",
        "categoryUuid": "123e4567-e89777-123e4567-e89",
        "supermarketUuid": "123e4567-e89-123e4567-e89788",
    }
    supermarket_category_pair = from_json(SupermarketCategoryPair, data)
    assert supermarket_category_pair.supermarket_category_pair_uuid == "123e4567-e89"
    assert supermarket_category_pair.category_uuid == "123e4567-e89777-123e4567-e89"
    assert supermarket_category_pair.supermarket_uuid == "123e4567-e89-123e4567-e89788"

def test__product__from_json_missing_field():
    data = {
        "supermarketCategoryPairUuid": "123e4567-e89",
        "categoryUuid": "123e4567-e89777-123e4567-e89",
    }
    supermarket_category_pair = from_json(SupermarketCategoryPair, data)
    assert supermarket_category_pair.supermarket_category_pair_uuid == "123e4567-e89"
    assert supermarket_category_pair.category_uuid == "123e4567-e89777-123e4567-e89"

def test__product__from_json_invalid_field():
    data = {
        "supermarketCategoryPairUuid": "123e4567-e89",
        "categoryUuid": "123e4567-e89777-123e4567-e89",
        "supermarketUuid": "123e4567-e89-123e4567-e89788",
        "invalidField": "test"
    }
    supermarket_category_pair = from_json(SupermarketCategoryPair, data)
    assert supermarket_category_pair.supermarket_category_pair_uuid == "123e4567-e89"
    assert supermarket_category_pair.category_uuid == "123e4567-e89777-123e4567-e89"
    assert supermarket_category_pair.supermarket_uuid == "123e4567-e89-123e4567-e89788"
    assert not hasattr(supermarket_category_pair, 'invalid_field')
