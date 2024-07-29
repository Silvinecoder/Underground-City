from flask import jsonify, Blueprint

from app.db.db_connection import create_session

from app.model.supermarket_category_pair import SupermarketCategoryPair

categories_blueprint = Blueprint("categories_blueprint", __name__)

# Define route to get all categories under a supermarket
@categories_blueprint.route("/supermarkets/<supermarket_uuid>/categories", methods=["GET"])
def get_categories_under_supermarket(supermarket_uuid):
    session = create_session()
    supermarket_category_pairs = session.query(SupermarketCategoryPair).filter_by(supermarket_uuid=supermarket_uuid).all()

    categories_json = []
    for pair in supermarket_category_pairs:
        category = pair.category
        categories_json.append(
            {
                "category_uuid": str(category.category_uuid),
                "category_name": category.category_name,
            }
        )

    session.close()
    return jsonify(categories_json), 200
