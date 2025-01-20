import pytest
from app.db.db_connection import refresh_session
from app.assistant.model_helper import from_json
from app.model.attribute import Attribute

ATTRIBUTE_UUID = "123e4567-e89"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    refresh_session()
    yield
    Attribute.get(ATTRIBUTE_UUID).delete()


def test__attribute__save_and_get():
    attribute = from_json(
        Attribute, {"attributeUuid": ATTRIBUTE_UUID, "attributeType": "test Attribute"}
    )
    attribute.uuid = ATTRIBUTE_UUID
    attribute.save()

    saved_attribute = Attribute.get(ATTRIBUTE_UUID)

    assert str(saved_attribute.uuid) == ATTRIBUTE_UUID
    assert saved_attribute.attribute_type == "test Attribute"
