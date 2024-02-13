from flask import Flask
from flask_restx import fields, Api

# Create flask app
app = Flask(__name__)
api = Api(app, title='Hello Fresh Orders Application',
          description='This application stores and retrieves order information')

orders_payload = api.model('Orders', {
    'user_id': fields.String(description='id of the user'),
    'product_code': fields.String(description='product code')
})

orders_response = api.model('OrderResponse', {
    'statusCode': fields.String(description='status code'),
    'message': fields.String(description='response message')
})
