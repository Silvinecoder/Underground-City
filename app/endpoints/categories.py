from flask import Flask, jsonify

from app.db.db_connection import create_session

from app.model.category import Category
from app.model.product import Product

# Create Flask application
app = Flask(__name__)

# Define route to get all categories
@app.route('/categories', methods=['GET'])
def get_products():
    session = create_session()
    categories = session.query(Category).all()
    session.close()

    categories_json = []
    for category in categories:
        categories_json.append({
            'category_uuid': str(category.category_uuid),
            'category_name': category.category_name
        })

    return jsonify(categories_json), 200

# Define route to get all products within a category
@app.route('/categories/<category_uuid>/products', methods=['GET'])
def get_products_by_category(category_uuid):
    session = create_session()
    products = session.query(Product).filter_by(product_category_uuid=category_uuid).all()
    session.close()

    products_json = []
    for product in products:
        products_json.append({
            'product_uuid': str(product.product_uuid),
            'name': product.product_name,
            'image': product.product_image,
        })

    return jsonify(products_json), 200