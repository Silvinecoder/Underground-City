from flask import jsonify, Blueprint
from app.db.db_connection import create_session
from app.model.attribute import Attribute
from app.model.product import Product

# Create Flask application
attributes_blueprint = Blueprint("attributes_blueprint", __name__)


# Define route to get all attributes
@attributes_blueprint.route("/attributes", methods=["GET"])
def get_attributes():
    session = create_session()
    try:
        attributes = session.query(Attribute).all()
        attribute_json = []
        for attribute in attributes:
            attribute_json.append(
                {
                    "attribute_uuid": attribute.attribute_uuid,
                    "attribute_type": attribute.attribute_type,
                }
            )
    finally:
        session.close()
    return jsonify(attribute_json), 200


# define route to get all products within an attribute
@attributes_blueprint.route("/attributes/<attribute_uuid>/products", methods=["GET"])
def get_products_by_attribute(attribute_uuid):
    session = create_session()
    try:
        attribute = (
            session.query(Attribute)
            .filter_by(attribute_uuid=attribute_uuid)
            .one_or_none()
        )
        if not attribute:
            session.close()
            return jsonify({"error": "Attribute not found"}), 404
        products = (
            session.query(Product)
            .filter_by(product_attribute_uuid=attribute.attribute_uuid)
            .all()
        )
        products_json = [
            {
                "product_uuid": str(product.product_uuid),
                "name": product.product_name,
                "image": product.product_image,
            }
            for product in products
        ]
    finally:
        session.close()

    return jsonify(products_json), 200


# define route to get a product within an attribute
@attributes_blueprint.route(
    "/attributes/<attribute_uuid>/products/<product_uuid>", methods=["GET"]
)
def get_product_by_attribute(attribute_uuid, product_uuid):
    session = create_session()
    try:
        product = (
            session.query(Product)
            .filter_by(product_uuid=product_uuid, product_attribute_uuid=attribute_uuid)
            .one_or_none()
        )
        if not product:
            session.close()
            return jsonify({"error": "Product not found for the given attribute"}), 404
        product_json = {
            "product_uuid": str(product.product_uuid),
            "name": product.product_name,
            "image": product.product_image,
        }
    finally:
        session.close()
    return jsonify(product_json), 200
