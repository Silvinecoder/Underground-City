from flask import jsonify, Blueprint

from app.db.db_connection import create_session

from app.model.supermarket_product_pair import SupermarketProductPair
from app.model.product import Product

products_blueprint = Blueprint("products_blueprint", __name__)


# Define route to get all products within a category in a supermarket
@products_blueprint.route(
    "/supermarkets/<supermarket_uuid>/categories/<category_uuid>/products",
    methods=["GET"],
)
def get_products_by_category_in_supermarket(supermarket_uuid, category_uuid):
    session = create_session()
    supermarket_product_pairs = (
        session.query(SupermarketProductPair)
        .filter_by(supermarket_uuid=supermarket_uuid)
        .all()
    )

    products_json = []
    for pair in supermarket_product_pairs:
        product = pair.product
        if str(product.product_category_uuid) == category_uuid:
            products_json.append(
                {
                    "product_uuid": str(product.product_uuid),
                    "name": product.product_name,
                    "image": product.product_image,
                    "price": product.product_price,
                }
            )

    session.close()
    return jsonify(products_json), 200


@products_blueprint.route("/products", methods=["GET"])
def get_products():
    session = create_session()

    # Query to get products and their associated supermarket UUIDs
    results = (
        session.query(Product, SupermarketProductPair.supermarket_uuid)
        .join(
            SupermarketProductPair,
            Product.product_uuid == SupermarketProductPair.product_uuid
        )
        .all()
    )

    # Dictionary to aggregate supermarket UUIDs by product UUID
    product_map = {}
    for product, supermarket_uuid in results:
        product_uuid_str = str(product.product_uuid)
        if product_uuid_str not in product_map:
            product_map[product_uuid_str] = {
                "product_uuid": product_uuid_str,
                "name": product.product_name,
                "image": product.product_image,
                "price": product.product_price,
                "supermarket_uuids": []
            }
        product_map[product_uuid_str]["supermarket_uuids"].append(str(supermarket_uuid))

    # Convert dictionary values to a list
    products_json = list(product_map.values())

    session.close()
    return jsonify(products_json), 200