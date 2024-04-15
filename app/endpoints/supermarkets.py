from flask import Flask, jsonify
from app.db.db_connection import create_session
from app.model.supermarket import Supermarket

# Create Flask application
app = Flask(__name__)

# Define route to get all supermarkets
@app.route('/supermarkets', methods=['GET'])
def get_products():
    session = create_session()
    supermarkets = session.query(Supermarket).all()
    session.close()

    supermarket_json = []
    for supermarket in supermarkets:
        supermarket_json.append({
            'supermarket_uuid': supermarket.supermarket_uuid,
            'supermarket_name': supermarket.supermarket_name,
            'country': supermarket.country
        })

    return jsonify(supermarket_json), 200