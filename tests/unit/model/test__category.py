from app.model.category import Category
from app.assistant.model_helper import from_json


def test__category__from_json_valid_data():
    data = {
        "categoryUuid": "8250b741-8948-471f-9350-bfcc0f37c8d5",
        "categoryName": "test category"
    }
    category = from_json(Category, data)
    assert category.category_uuid == "8250b741-8948-471f-9350-bfcc0f37c8d5"
    assert category.category_name == "test category"

def test__category__from_json_missing_field():
    data = {
        "categoryUuid": "8250b741-8948-471f-9350-bfcc0f37c8d5"
    }
    category = from_json(Category, data)
    assert category.category_uuid == "8250b741-8948-471f-9350-bfcc0f37c8d5"
    assert category.category_name is None

def test__category__from_json_invalid_field():
    data = {
        "categoryUuid": "8250b741-8948-471f-9350-bfcc0f37c8d5",
        "invalidField": "test"
    }
    category = from_json(Category, data)
    assert category.category_uuid == "8250b741-8948-471f-9350-bfcc0f37c8d5"
    assert not hasattr(category, 'invalid_field')