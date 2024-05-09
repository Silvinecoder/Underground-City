from flask import Flask, jsonify
from app.db.db_connection import create_session

from app.model.attribute import Attribute
from app.model.product import Product

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

# define route to get all products within an attribute
@app.route('/attributes/products', methods=['GET'])
def get_attributes_with_products():
    session = create_session()
    attributes = session.query(Attribute).all()
    session.close()

    attributes_json = []
    for attribute in attributes:
        products = session.query(Product).filter_by(product_attribute_uuid=attribute.attribute_uuid).all()

        products_json = []
        for product in products:
            products_json.append({
                'product_uuid': str(product.product_uuid),
                'name': product.product_name,
                'image': product.product_image,
            })

        attributes_json.append({
            'attribute_uuid': attribute.attribute_uuid,
            'attribute_type': attribute.attribute_type,
            'products': products_json
        })

    return jsonify(attributes_json), 200

# Define route to get all attributes within a product
@app.route('/products/attributes', methods=['GET'])
def get_products_with_attributes():
    session = create_session()
    products = session.query(Product).all()
    session.close()

    products_json = []
    for product in products:
        attributes = session.query(Attribute).filter_by(attribute_uuid=product.product_attribute_uuid).all()

        attributes_json = []
        for attribute in attributes:
            attributes_json.append({
                'attribute_uuid': attribute.attribute_uuid,
                'attribute_type': attribute.attribute_type
            })

        products_json.append({
            'product_uuid': str(product.product_uuid),
            'name': product.product_name,
            'image': product.product_image,
            'attributes': attributes_json
        })

    return jsonify(products_json), 200

# Define route to get all attributes within a single product
@app.route('/products/<product_uuid>/attributes', methods=['GET'])
def get_product_with_attributes(product_uuid):
    session = create_session()
    product = session.query(Product).filter_by(product_uuid=product_uuid).first()
    session.close()

    attributes = session.query(Attribute).filter_by(attribute_uuid=product.product_attribute_uuid).all()

    attributes_json = []
    for attribute in attributes:
        attributes_json.append({
            'attribute_uuid': attribute.attribute_uuid,
            'attribute_type': attribute.attribute_type
        })

    product_json = {
        'product_uuid': str(product.product_uuid),
        'name': product.product_name,
        'image': product.product_image,
        'attributes': attributes_json
    }

    return jsonify(product_json), 200


