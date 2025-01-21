import pytest
from app.db.db_connection import refresh_session
from app.assistant.model_helper import from_json
from app.model.supermarket import Supermarket

SUPERMARKET_UUID = "41396390-3609-4872-8609-86992873fe48"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    session = refresh_session()
    yield
    supermarket = (
        session.query(Supermarket).filter_by(supermarket_uuid=SUPERMARKET_UUID).first()
    )
    if supermarket:
        session.delete(supermarket)


def test__attribute__save_and_get():
    session = refresh_session()
    supermarket = from_json(
        Supermarket,
        {
            "supermarketUuid": SUPERMARKET_UUID,
            "supermarketName": "test supermarket",
            "supermarketCountry": "test country",
        },
    )
    supermarket.uuid = SUPERMARKET_UUID
    session.add(supermarket)

    saved_supermarket = (
        session.query(Supermarket).filter_by(supermarket_uuid=SUPERMARKET_UUID).one()
    )

    assert str(saved_supermarket.supermarket_uuid) == SUPERMARKET_UUID
    assert saved_supermarket.supermarket_name == "test supermarket"
    assert saved_supermarket.supermarket_country == "test country"
