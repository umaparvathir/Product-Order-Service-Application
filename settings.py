import os

# Application settings
HOST = "0.0.0.0"
PORT = 5000
URL_PREFIX = ""

# Swagger settings
SWAGGER_UI_DOC_EXPANSION = True

# Database settings
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']
PRODUCT_TABLE_NAME = "product_info"
USER_TABLE_NAME = "user_info"

# Rabbitmq broker settings
RBMQ_HOST = "rabbitmq"
RBMQ_PORT = 5672
RBMQ_EXCHANGE = "orders"
RBMQ_ROUTING_KEY = "created_order"
RABBITMQ_DEFAULT_USER = os.environ['RABBITMQ_DEFAULT_USER']
RABBITMQ_DEFAULT_PASS = os.environ['RABBITMQ_DEFAULT_PASS']

# Endpoints
USER_SVC_ENDPOINT = "http://user-service:8080/users/"
PRODUCT_SVC_ENDPOINT = "http://product-service:8080/products/"