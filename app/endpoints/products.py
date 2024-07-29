from flask import jsonify, Blueprint

from app.db.db_connection import create_session

from app.model.supermarket_product_pair import SupermarketProductPair

products_blueprint = Blueprint("products_blueprint", __name__)

# Define route to get all products within a category in a supermarket
@products_blueprint.route("/supermarkets/<supermarket_uuid>/categories/<category_uuid>/products", methods=["GET"])
def get_products_by_category_in_supermarket(supermarket_uuid, category_uuid):
    session = create_session()
    supermarket_product_pairs = session.query(SupermarketProductPair).filter_by(supermarket_uuid=supermarket_uuid).all()

    products_json = []
    for pair in supermarket_product_pairs:
        product = pair.product
        if str(product.product_category_uuid) == category_uuid:
            products_json.append(
                {
                    "product_uuid": str(product.product_uuid),
                    "name": product.product_name,
                    "image": product.product_image,
                }
            )

    session.close()
    return jsonify(products_json), 200
