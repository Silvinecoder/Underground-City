from app.model.supermarket import Supermarket
from app.assistant.model_helper import from_json

def test__supermarket__from_json_valid_data():
    data = {
        "supermarketUuid": "123e4567-e89b-12d3-a456-426614174000",
        "supermarketName": "test supermarket",
        "supermarketCountry": "test country"
    }
    supermarket = from_json(Supermarket, data)
    assert supermarket.supermarket_uuid == "123e4567-e89b-12d3-a456-426614174000"
    assert supermarket.supermarket_name == "test supermarket"
    assert supermarket.supermarket_country == "test country"

def test__attribute__from_json_missing_field():
    data = {
        "supermarketUuid": "123e4567-e89b-12d3-a456-426614174000"
    }
    supermarket = from_json(Supermarket, data)
    assert supermarket.supermarket_uuid == "123e4567-e89b-12d3-a456-426614174000"
    assert supermarket.supermarket_name is None

def test__attribute__from_json_invalid_field():
    data = {
        "supermarketUuid": "123e4567-e89b-12d3-a456-426614174000",
        "invalidField": "test"
    }
    supermarket = from_json(Supermarket, data)
    assert supermarket.supermarket_uuid == "123e4567-e89b-12d3-a456-426614174000"
    assert not hasattr(supermarket, 'invalid_field')
