from flask import jsonify, Blueprint
from app.db.db_connection import create_session

from app.model.supermarket import Supermarket
from app.model.product import Product
from app.model.supermarket_category_pair import SupermarketCategoryPair
from app.model.supermarket_product_pair import SupermarketProductPair

supermarkets_blueprint = Blueprint("supermarkets_blueprint", __name__)


# Define route to get all supermarkets
@supermarkets_blueprint.route("/supermarkets", methods=["GET"])
def get_supermarkets():
    session = create_session()
    try:
        supermarkets = session.query(Supermarket).all()
        session.close()
        supermarket_json = []
        for supermarket in supermarkets:
            supermarket_json.append(
                {
                    "supermarket_uuid": str(supermarket.supermarket_uuid),
                    "supermarket_name": supermarket.supermarket_name,
                    "supermarket_country": supermarket.supermarket_country,
                }
            )
    finally:
        session.close()
    return jsonify(supermarket_json), 200


# Define route to get a supermarket by its uuid
@supermarkets_blueprint.route("/supermarkets/<supermarket_uuid>", methods=["GET"])
def get_supermarket_by_uuid(supermarket_uuid):
    session = create_session()
    try:
        supermarket = (
            session.query(Supermarket)
            .filter_by(supermarket_uuid=supermarket_uuid)
            .first()
        )
        if not supermarket:
            session.close()
            return jsonify({"error": "Supermarket not found"}), 404
        supermarket_json = {
            "supermarket_uuid": str(supermarket.supermarket_uuid),
            "supermarket_name": supermarket.supermarket_name,
            "supermarket_country": supermarket.supermarket_country,
        }
    finally:
        session.close()
    return jsonify(supermarket_json), 200


# Define route to get all categories under a supermarket
@supermarkets_blueprint.route(
    "/supermarkets/<supermarket_uuid>/categories", methods=["GET"]
)
def get_categories_under_supermarket(supermarket_uuid):
    session = create_session()
    try:
        supermarket_category_pairs = (
            session.query(SupermarketCategoryPair)
            .filter_by(supermarket_uuid=supermarket_uuid)
            .all()
        )
        categories_json = []
        for pair in supermarket_category_pairs:
            category = pair.category
            categories_json.append(
                {
                    "category_uuid": str(category.category_uuid),
                    "category_name": category.category_name,
                }
            )
    finally:
        session.close()
    return jsonify(categories_json), 200


# Define route to get a category under a supermarket
@supermarkets_blueprint.route(
    "/supermarkets/<supermarket_uuid>/categories/<category_uuid>", methods=["GET"]
)
def get_category_under_supermarket(supermarket_uuid, category_uuid):
    session = create_session()
    try:
        supermarket_category_pair = (
            session.query(SupermarketCategoryPair)
            .filter_by(supermarket_uuid=supermarket_uuid, category_uuid=category_uuid)
            .one_or_none()
        )
        if not supermarket_category_pair:
            session.close()
            return jsonify({"error": "Category not found under this supermarket"}), 404
        category = supermarket_category_pair.category
        category_json = {
            "category_uuid": str(category.category_uuid),
            "category_name": category.category_name,
        }
    finally:
        session.close()
    return jsonify(category_json), 200


# Define route to get all products within a category in a supermarket
@supermarkets_blueprint.route(
    "/supermarkets/<supermarket_uuid>/categories/<category_uuid>/products",
    methods=["GET"],
)
def get_products_by_category_in_supermarket(supermarket_uuid, category_uuid):
    session = create_session()
    try:
        supermarket = (
            session.query(Supermarket)
            .filter_by(supermarket_uuid=supermarket_uuid)
            .one_or_none()
        )
        if not supermarket:
            session.close()
            return jsonify({"error": "Supermarket not found"}), 404
        supermarket_category_pair = (
            session.query(SupermarketCategoryPair)
            .filter_by(supermarket_uuid=supermarket_uuid, category_uuid=category_uuid)
            .first()
        )
        if not supermarket_category_pair:
            session.close()
            return jsonify({"error": "Category not found under this supermarket"}), 404
        products = (
            session.query(Product).filter_by(product_category_uuid=category_uuid).all()
        )
        products_json = [
            {
                "product_uuid": str(product.product_uuid),
                "name": product.product_name,
                "image": product.product_image,
                "price": product.product_price,
                "supermarket_name": supermarket.supermarket_name,
            }
            for product in products
        ]
    finally:
        session.close()
    return jsonify(products_json), 200


# Define route to get a product within a category in a supermarket
@supermarkets_blueprint.route(
    "/supermarkets/<supermarket_uuid>/categories/<category_uuid>/products/<product_uuid>",
    methods=["GET"],
)
def get_product_by_category_in_supermarket(
    supermarket_uuid, category_uuid, product_uuid
):
    session = create_session()
    try:
        supermarket = (
            session.query(Supermarket)
            .filter_by(supermarket_uuid=supermarket_uuid)
            .one_or_none()
        )
        if not supermarket:
            session.close()
            return jsonify({"error": "Supermarket not found"}), 404
        supermarket_category_pair = (
            session.query(SupermarketCategoryPair)
            .filter_by(supermarket_uuid=supermarket_uuid, category_uuid=category_uuid)
            .one_or_none()
        )
        if not supermarket_category_pair:
            session.close()
            return jsonify({"error": "Category not found under this supermarket"}), 404
        product = (
            session.query(Product)
            .filter_by(product_uuid=product_uuid, product_category_uuid=category_uuid)
            .one_or_none()
        )
        if not product:
            session.close()
            return jsonify({"error": "Product not found under this category"}), 404
        product_json = {
            "product_uuid": str(product.product_uuid),
            "name": product.product_name,
            "image": product.product_image,
            "price": product.product_price,
            "supermarket_name": supermarket.supermarket_name,
        }
    finally:
        session.close()
    return jsonify(product_json), 200


# Define route to get all products within a supermarket
@supermarkets_blueprint.route(
    "/supermarkets/<supermarket_uuid>/products", methods=["GET"]
)
def get_products_by_supermarket(supermarket_uuid):
    session = create_session()
    try:
        supermarket = (
            session.query(Supermarket)
            .filter_by(supermarket_uuid=supermarket_uuid)
            .one_or_none()
        )
        if not supermarket:
            session.close()
            return jsonify({"error": "Supermarket not found"}), 404
        pairs = (
            session.query(SupermarketProductPair)
            .filter_by(supermarket_uuid=supermarket_uuid)
            .all()
        )
        if not pairs:
            session.close()
            return jsonify({"error": "No products found for this supermarket"}), 404
        products_json = [
            {
                "product_uuid": str(pair.product.product_uuid),
                "name": pair.product.product_name,
                "image": pair.product.product_image,
                "price": pair.product.product_price,
                "supermarket_name": supermarket.supermarket_name,
            }
            for pair in pairs
        ]
    finally:
        session.close()
    return jsonify(products_json), 200


# Define route to get a product within a supermarket
@supermarkets_blueprint.route(
    "/supermarkets/<supermarket_uuid>/products/<product_uuid>", methods=["GET"]
)
def get_product_by_supermarket(supermarket_uuid, product_uuid):
    session = create_session()
    try:
        supermarket = (
            session.query(Supermarket)
            .filter_by(supermarket_uuid=supermarket_uuid)
            .one_or_none()
        )
        if not supermarket:
            session.close()
            return jsonify({"error": "Supermarket not found"}), 404
        pair = (
            session.query(SupermarketProductPair)
            .filter_by(supermarket_uuid=supermarket_uuid, product_uuid=product_uuid)
            .first()
        )
        if not pair:
            session.close()
            return jsonify({"error": "Product not found in this supermarket"}), 404
        product_json = {
            "product_uuid": str(pair.product.product_uuid),
            "name": pair.product.product_name,
            "image": pair.product.product_image,
            "price": pair.product.product_price,
            "supermarket_name": supermarket.supermarket_name,
        }
    finally:
        session.close()
    return jsonify(product_json), 200
