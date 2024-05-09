from flask import Flask, jsonify
from app.db.db_connection import create_session
from app.model.supermarket import Supermarket
from app.model.supermarket_product_pair import SupermarketProductPair

# Create Flask application
app = Flask(__name__)

# Define route to get all supermarkets
@app.route('/supermarkets', methods=['GET'])
def get_supermarkets():
    session = create_session()
    supermarkets = session.query(Supermarket).all()
    session.close()

    supermarket_json = []
    for supermarket in supermarkets:
        supermarket_json.append({
            'supermarket_uuid': supermarket.supermarket_uuid,
            'supermarket_name': supermarket.supermarket_name,
            'supermarket_country': supermarket.supermarket_country
        })

    return jsonify(supermarket_json), 200

# Define route to get all supermarkets within a product
@app.route('/supermarkets/products', methods=['GET'])
def get_supermarkets_with_products():
    session = create_session()
    supermarkets = session.query(Supermarket).all()
    session.close()

    supermarkets_json = []
    for supermarket in supermarkets:
        supermarket_product_pair = session.query(SupermarketProductPair).filter_by(supermarket_uuid=supermarket.supermarket_uuid).all()

        products_json = []
        for product in supermarket_product_pair:
            products_json.append({
                'product_uuid': str(product.product_uuid),
                'name': product.product_name,
                'image': product.product_image,
            })

        supermarkets_json.append({
            'supermarket_uuid': supermarket.supermarket_uuid,
            'supermarket_name': supermarket.supermarket_name,
            'products': products_json
        })

    return jsonify(supermarkets_json), 200