from flask_restx import fields
from serializers.order_body_serializers import api

product_svc_response = api.model('Products', {
    'code': fields.String(description='product code'),
    'name': fields.String(description='product name'),
    'price': fields.Float(description='total amount for the product')
})

"""
product_svc_response = api.model('ProductServiceResponse', {
    'response': fields.List(fields.Nested(products)),
    'statusCode': fields.Integer(description='status code'),
    'message': fields.String(description='response message')
})
"""