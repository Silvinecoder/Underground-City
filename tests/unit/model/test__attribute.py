from app.model.attribute import Attribute
from app.assistant.model_helper import from_json

def test__attribute__from_json_valid_data():
    data = {
        "attributeUuid": "123e4567-e89b-12d3-a456-426614174000",
        "attributeType": "test attribute"
    }
    attribute = from_json(Attribute, data)
    assert attribute.attribute_uuid == "123e4567-e89b-12d3-a456-426614174000"
    assert attribute.attribute_type == "test attribute"

def test__attribute__from_json_missing_field():
    data = {
        "attributeUuid": "123e4567-e89b-12d3-a456-426614174000"
    }
    attribute = from_json(Attribute, data)
    assert attribute.attribute_uuid == "123e4567-e89b-12d3-a456-426614174000"
    assert attribute.attribute_type is None

def test__attribute__from_json_invalid_field():
    data = {
        "attributeUuid": "123e4567-e89b-12d3-a456-426614174000",
        "invalidField": "test"
    }
    attribute = from_json(Attribute, data)
    assert attribute.attribute_uuid == "123e4567-e89b-12d3-a456-426614174000"
    assert not hasattr(attribute, 'invalid_field')
