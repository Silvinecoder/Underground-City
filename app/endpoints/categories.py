from flask import Flask, jsonify
from flask_cors import CORS
from app.db.db_connection import create_session
from collections import defaultdict
from app.model.product import Product

# Create Flask application
app = Flask(__name__)
CORS(app)  # Initialize Flask-CORS

# Define route to get all products
@app.route('/categories/products', methods=['GET'])
def get_products_by_category():
    with app.app_context():  # Ensure execution within Flask application context
        session = create_session()
        products = session.query(Product).all()
        session.close()

        # Group products by category
        categories_with_products = defaultdict(list)
        for product in products:
            categories_with_products[product.category].append({
                'product_uuid': str(product.product_uuid),
                'name': product.name,
                'image': product.image,
                'supermarket': product.supermarket,
                'country': product.country
            })

        return jsonify(categories_with_products), 200

if __name__ == "__main__":
    app.run(debug=True)
