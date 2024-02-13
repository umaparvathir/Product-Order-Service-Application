import pytest
import os
from mock import patch
import json
    
    # mock env variables for testing purpose
with patch.dict(os.environ, {'DB_HOST': 'mock-value', 'DB_USER': 'mock-value', 'DB_PASSWORD': 'mock-value',\
'DB_NAME': 'mock-value','RABBITMQ_DEFAULT_USER': 'mock-value','RABBITMQ_DEFAULT_PASS': 'mock-value'}):
    from api import order_service_api
    from serializers.order_body_serializers import app   

    @pytest.fixture
    def client():
        app.config.update({"TESTING": True})
        with app.test_client() as client:
            yield client

    # product_code is not added in request
    def test_order_service_fail1(client):
        response = client.post("/orders",data='{"user_id":"abc"}',headers={"Content-Type": "application/json"})
        response = json.loads(response.data)
        assert response['statusCode'] == '500'
        assert response['message'] == 'product_code is missing in the request body'

    # user_id is not added in request
    def test_order_service_fail2(client):
        response = client.post("/orders",data='{"product_code":"abc"}',headers={"Content-Type": "application/json"})
        response = json.loads(response.data)
        assert response['statusCode'] == '500'
        assert response['message'] == 'user_id is missing in the request body'

    # Test success scenerio
    @patch('api.order_service_api.OrderService.order_service_method')
    def test_order_service_success(svc_method,client):
        
        # Mock successful result
        message = """sent message {'producer': 'Order-Service', 'sent_at': '2023-11-29 19:37:58',
        'type': 'json', 'payload': {'order': {'order_id': '20231129193759720751','customer_fullname': 'Ada Lovelace',
   		'product_name': 'Classic Box', 'total_amount': 9.99, 'created_at': '2023-11-29 19:37:59'}}}"""
        svc_method.return_value = {'statusCode': 200,'message': message}

        # Send correct request
        response = client.post("/orders",data='{"user_id":"7c11e1ce2741","product_code":"classic-box"}',headers={"Content-Type": "application/json"})
        response = json.loads(response.data)
        print(response)
        assert response['statusCode'] == '200'

    
        