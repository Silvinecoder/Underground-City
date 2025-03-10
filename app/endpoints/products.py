from flask import jsonify, Blueprint

from app.db.db_connection import create_session

from app.model.product import Product
from app.model.supermarket_product_pair import SupermarketProductPair
from app.model.supermarket import Supermarket

products_blueprint = Blueprint("products_blueprint", __name__)


# Define route to get the products
@products_blueprint.route("/products", methods=["GET"])
def get_products():
    session = create_session()
    try:
        products = session.query(Product).all()
        products_json = []

        for product in products:
            # Get the supermarkets associated with this product through the SupermarketProductPair
            supermarkets = (
                session.query(Supermarket)
                .join(SupermarketProductPair)
                .filter(SupermarketProductPair.product_uuid == product.product_uuid)
                .all()
            )

            product_json = {
                "product_uuid": str(product.product_uuid),
                "name": product.product_name,
                "image": product.product_image,
                "price": product.product_price,
                "supermarkets": [
                    {
                        "supermarket_uuid": str(supermarket.supermarket_uuid),
                        "supermarket_name": supermarket.supermarket_name,
                    }
                    for supermarket in supermarkets
                ],
            }
            products_json.append(product_json)
    finally:
        session.close()

    return jsonify(products_json), 200


# Define route to get a product by its uuid
@products_blueprint.route("/products/<product_uuid>", methods=["GET"])
def get_product_by_uuid(product_uuid):
    session = create_session()
    try:
        product = session.query(Product).filter_by(product_uuid=product_uuid).first()
        if not product:
            session.close()
            return jsonify({"error": "Product not found"}), 404
        product_json = {
            "product_uuid": str(product.product_uuid),
            "name": product.product_name,
            "image": product.product_image,
            "price": product.product_price,
        }
    finally:
        session.close()
    return jsonify(product_json), 200
