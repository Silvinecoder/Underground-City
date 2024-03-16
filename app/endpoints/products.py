from flask import Flask, jsonify
from app.db.db_connection import create_session
from app.model.product import Product

# Create Flask application
app = Flask(__name__)

# Define route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    session = create_session()
    products = session.query(Product).all()
    session.close()

    # Convert products to JSON format
    products_json = []
    for product in products:
        products_json.append({
            'product_uuid': str(product.product_uuid),
            'name': product.name,
            'image': product.image,
            'category': product.category,
            'supermarket': product.supermarket,
            'country': product.country
        })

    return jsonify(products_json), 200
