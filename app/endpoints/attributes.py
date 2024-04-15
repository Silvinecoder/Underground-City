from flask import Flask, jsonify
from app.db.db_connection import create_session
from app.model.attribute import Attribute

# Create Flask application
app = Flask(__name__)

# Define route to get all attributes
@app.route('/attributes', methods=['GET'])
def get_products():
    session = create_session()
    attributes = session.query(Attribute).all()
    session.close()

    attribute_json = []
    for attribute in attributes:
        attribute_json.append({
            'attribute_uuid': attribute.attribute_uuid,
            'attribute_type': attribute.attribute_type
        })

    return jsonify(attribute_json), 200