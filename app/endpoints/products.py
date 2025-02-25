from flask import jsonify, Blueprint

from app.db.db_connection import create_session

from app.model.product import Product

products_blueprint = Blueprint("products_blueprint", __name__)


# Define route to get the products
@products_blueprint.route("/products", methods=["GET"])
def get_products():
    session = create_session()
    try:
        products = session.query(Product).all()
        products_json = [
            {
                "product_uuid": str(product.product_uuid),
                "name": product.product_name,
                "image": product.product_image,
                "price": product.product_price,
            }
            for product in products
        ]
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
