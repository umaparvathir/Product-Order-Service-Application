from flask_restx import fields
from serializers.order_body_serializers import api

users = api.model('Users', {
    'user_id': fields.String(description='user id'),
    'customer_fullname': fields.String(description='customer name')
})

user_svc_response = api.model('UserServiceResponse', {
    'response': fields.List(fields.Nested(users)),
    'statusCode': fields.Integer(description='status code'),
    'message': fields.String(description='response message')
})