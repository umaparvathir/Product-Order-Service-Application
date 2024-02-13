from flask import Flask, request
from flask_restx import Resource

from serializers.order_body_serializers import api, orders_payload, orders_response
from service.order_service import OrderService

# Create namespace for orders service
ns = api.namespace("", description="Order Service Application")

@ns.route("/orders")
class OrderDetails(Resource):
    @api.expect(orders_payload) # Expect input format
    @api.marshal_with(orders_response) # Expect response in specific format
    def post(self):

        # Extract json from request
        order_data = request.get_json()

        # Ensure user_id is not empty/missing
        if 'user_id' not in order_data or order_data["user_id"] == "":
            response = {
                'statusCode': 500,
                'message': 'user_id is missing in the request body'
            }
            return response
        
        # Ensure product_code is not empty/missing
        if 'product_code' not in order_data or order_data["product_code"] == "":
            response = {
                'statusCode': 500,
                'message': 'product_code is missing in the request body'
            }
            return response

        response = OrderService().order_service_method(order_data)

        return response