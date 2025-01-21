import pytest
from app.db.db_connection import refresh_session
from app.assistant.model_helper import from_json
from app.model.supermarket import Supermarket
from app.model.category import Category
from app.model.supermarket_category_pair import SupermarketCategoryPair

SUPERMARKET_UUID = "07c1904a-67ef-46f8-90fb-4d04e6c759c5"
CATEGORY_UUID = "ccbcde92-32a7-4d2c-ab71-bd6f7d4e865e"
SUPERMARKET_CATEGORY_PAIR_UUID = "41396390-3609-4872-8609-86992873fe48"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    session = refresh_session()
    yield
    try:
        supermarket_category_pair = (
            session.query(SupermarketCategoryPair)
            .filter_by(supermarket_category_pair_uuid=SUPERMARKET_CATEGORY_PAIR_UUID)
            .first()
        )
        if supermarket_category_pair:
            session.delete(supermarket_category_pair)

        supermarket = (
            session.query(Supermarket)
            .filter_by(supermarket_uuid=SUPERMARKET_UUID)
            .first()
        )
        if supermarket:
            session.delete(supermarket)

        category = (
            session.query(Category).filter_by(category_uuid=CATEGORY_UUID).first()
        )
        if category:
            session.delete(category)

        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def test__product__save_and_get():
    session = refresh_session()

    supermarket = from_json(
        Supermarket,
        {
            "supermarketUuid": SUPERMARKET_UUID,
            "supermarketName": "test Supermarket",
            "supermarketCountry": "test UK",
        },
    )
    session.add(supermarket)
    session.commit()
    saved_supermarket = (
        session.query(Supermarket).filter_by(supermarket_uuid=SUPERMARKET_UUID).one()
    )

    category = from_json(
        Category, {"categoryUuid": CATEGORY_UUID, "categoryName": "test Category"}
    )
    session.add(category)
    session.commit()
    saved_category = (
        session.query(Category).filter_by(category_uuid=CATEGORY_UUID).one()
    )

    supermarket_category_pair = from_json(
        SupermarketCategoryPair,
        {
            "supermarketCategoryPairUuid": SUPERMARKET_CATEGORY_PAIR_UUID,
            "categoryUuid": CATEGORY_UUID,
            "supermarketUuid": SUPERMARKET_UUID,
        },
    )
    session.add(supermarket_category_pair)
    session.commit()

    saved_supermarket_category_pair = (
        session.query(SupermarketCategoryPair)
        .filter_by(supermarket_category_pair_uuid=SUPERMARKET_CATEGORY_PAIR_UUID)
        .one()
    )

    assert str(saved_supermarket_category_pair.supermarket_category_pair_uuid)== SUPERMARKET_CATEGORY_PAIR_UUID
    assert str(saved_category.category_uuid) == CATEGORY_UUID
    assert str(saved_supermarket.supermarket_uuid) == SUPERMARKET_UUID
