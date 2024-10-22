from flask import Flask
from flask_cors import CORS
import awsgi

from app.endpoints.products import products_blueprint
from app.endpoints.categories import categories_blueprint
from app.endpoints.supermarkets import supermarkets_blueprint

# Initialize the Flask app
app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

# Register blueprints for different endpoints
app.register_blueprint(products_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(supermarkets_blueprint)

# Define the Lambda handler
def lambda_handler(event, context):
    return awsgi.response(app, event, context)

# If you want to run locally with flask (optional)
if __name__ == "__main__":
    app.run()
