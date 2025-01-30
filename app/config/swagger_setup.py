from flask_swagger_ui import get_swaggerui_blueprint
import os

def setup_swagger_ui(app, path_to_openapi=''):
    # Get full path from current script's directory up to openapi folder
    openapi_file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        path_to_openapi,
        'openapi.yaml'
    )

    if not os.path.exists(openapi_file_path):
        raise FileNotFoundError(f"OpenAPI YAML file not found at {openapi_file_path}")

    # Swagger UI setup for the app
    blueprints = get_swaggerui_blueprint(
        "/docs",
        f"{os.path.relpath(openapi_file_path, __file__)}",
        config={"app_name": "Underground City API"}
    )

    # Serve the OpenAPI schema at /static/openapi.yml using send_from_directory
    app.register_blueprint(blueprints)