from flask import Flask, jsonify
from flask_cors import CORS
from app.db.db_connection import create_session
from collections import defaultdict
from app.model.product import Product
from app.model.category import Category

# Create Flask application
app = Flask(__name__)
CORS(app)  # Initialize Flask-CORS

# Define route to get all categories
@app.route('/categories', methods=['GET'])
def get_products():
    session = create_session()
    categories = session.query(Category).all()
    session.close()

    attribute_json = []
    for category in categories:
        attribute_json.append({
            'attribute_uuid': category.attribute_uuid,
            'attribute_type': category.attribute_type
        })

    return jsonify(attribute_json), 200

# Define route to get all products within a category
@app.route('/categories/products', methods=['GET'])
def get_products_by_category():
    with app.app_context():  # Ensure execution within Flask application context
        session = create_session()
        products = session.query(Product).all()
        session.close()

        # Group products by category
        categories_with_products = defaultdict(list)
        for product in products:
            category_name = product.product_category.category_name
            product_data = {
                'product_uuid': str(product.product_uuid),
                'name': product.product_name,
                'image': product.product_image,
                'attribute': product.product_attribute.attribute_type,
                'supermarket': [pair.supermarket.supermarket_name for pair in product.supermarket_product_pair],
                'country': [pair.supermarket.country for pair in product.supermarket_product_pair]
            }
            categories_with_products[category_name].append(product_data)

        return jsonify(dict(categories_with_products)), 200

if __name__ == "__main__":
    app.run(debug=True)
