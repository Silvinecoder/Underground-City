from flask import Flask
from flask_cors import CORS

from app.endpoints.products import products_blueprint
from app.endpoints.categories import categories_blueprint
from app.endpoints.supermarkets import supermarkets_blueprint


app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

app.register_blueprint(products_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(supermarkets_blueprint)
