import pytest
from app.db.db_connection import refresh_session
from app.assistant.model_helper import from_json
from app.model.category import Category

CATEGORY_UUID = "41396390-3609-4872-8609-86992873fe48"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    session = refresh_session()
    yield
    category = session.query(Category).filter_by(category_uuid=CATEGORY_UUID).first()
    if category:
        session.delete(category)


def test__attribute__save_and_get():
    session = refresh_session()
    category = from_json(
        Category, {"categoryUuid": CATEGORY_UUID, "categoryName": "test Category"}
    )
    category.uuid = CATEGORY_UUID
    session.add(category)

    saved_category = session.query(Category).filter_by(category_uuid=CATEGORY_UUID).one()

    assert str(saved_category.category_uuid) == CATEGORY_UUID
    assert saved_category.category_name == "test Category"
