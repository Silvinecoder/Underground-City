from flask import jsonify, Blueprint
from app.db.db_connection import create_session

from app.model.supermarket import Supermarket

supermarkets_blueprint = Blueprint("supermarkets_blueprint", __name__)

# Define route to get all supermarkets
@supermarkets_blueprint.route("/supermarkets", methods=["GET"])
def get_supermarkets():
    session = create_session()
    supermarkets = session.query(Supermarket).all()
    session.close()

    supermarket_json = []
    for supermarket in supermarkets:
        supermarket_json.append(
            {
                "supermarket_uuid": str(supermarket.supermarket_uuid),
                "supermarket_name": supermarket.supermarket_name,
                "supermarket_country": supermarket.supermarket_country,
            }
        )

    return jsonify(supermarket_json), 200
