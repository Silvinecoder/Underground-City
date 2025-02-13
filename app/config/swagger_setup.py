from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory
import os


def get_swagger_config():
    return {
        'app_name': "Underground City API",
        'deepLinking': True,
        'supportedSubmitMethods': ['get', 'post', 'put', 'delete']
    }

def create_swagger_blueprint(openapi_url):
    return get_swaggerui_blueprint(
        '/docs',
        openapi_url,
        config=get_swagger_config()
    )

def setup_swagger_ui(app, path_to_openapi='openapi'):
    # Get absolute path to the openapi directory
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    openapi_dir = os.path.join(base_dir, path_to_openapi)
    
    # Path to main OpenAPI file
    main_openapi_path = os.path.join(openapi_dir, 'openapi.yaml')
    
    if not os.path.exists(main_openapi_path):
        raise FileNotFoundError(f"OpenAPI YAML file not found at {main_openapi_path}")
    
    # Route to serve the OpenAPI files from the openapi directory
    @app.route('/openapi/<path:filename>')
    def serve_openapi_file(filename):
        return send_from_directory(openapi_dir, filename)
    
    # Create and register blueprint using configuration
    swagger_blueprint = create_swagger_blueprint('/openapi/openapi.yaml')
    app.register_blueprint(swagger_blueprint)