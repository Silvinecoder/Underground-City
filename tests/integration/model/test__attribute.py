import pytest
from app.db.db_connection import refresh_session
from app.assistant.model_helper import from_json
from app.model.attribute import Attribute

ATTRIBUTE_UUID = "41396390-3609-4872-8609-86992873fe48"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    session = refresh_session()
    yield
    attribute = session.query(Attribute).filter_by(attribute_uuid=ATTRIBUTE_UUID).first()
    if attribute:
        session.delete(attribute)


def test__attribute__save_and_get():
    session = refresh_session()
    attribute = from_json(
        Attribute, {"attributeUuid": ATTRIBUTE_UUID, "attributeType": "test Attribute"}
    )
    attribute.uuid = ATTRIBUTE_UUID
    session.add(attribute)

    saved_attribute = session.query(Attribute).filter_by(attribute_uuid=ATTRIBUTE_UUID).one()

    assert str(saved_attribute.attribute_uuid) == ATTRIBUTE_UUID
    assert saved_attribute.attribute_type == "test Attribute"
