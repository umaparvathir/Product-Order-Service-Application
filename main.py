from waitress import serve
from flask import Blueprint
import logging

import settings
from serializers.order_body_serializers import app, api
from api.order_service_api import ns as order_namespace

# Setting log level to INFO
logging.basicConfig(level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

def initialize_app(flask_app):

    # Register Blueprint
    blueprint = Blueprint('api', __name__, url_prefix=settings.URL_PREFIX)
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)

    # Add namespace for all services
    api.add_namespace(order_namespace)

    # Configure Swagger documentation
    app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.SWAGGER_UI_DOC_EXPANSION

if __name__ == "__main__":
    initialize_app(app)

    # Run the application
    serve(app, host=settings.HOST, port=settings.PORT)
    #app.run(host=settings.HOST, port=settings.PORT,debug=True)

    
