import pytest
import os
from mock import patch

# mock env variables for testing purpose
with patch.dict(os.environ, {'DB_HOST': 'mock-value', 'DB_USER': 'mock-value', 'DB_PASSWORD': 'mock-value',\
'DB_NAME': 'mock-value','RABBITMQ_DEFAULT_USER': 'mock-value','RABBITMQ_DEFAULT_PASS': 'mock-value'}):
    from service import order_service

    @patch('service.order_service.OrderServiceQuery.order_service_query')
    def test_order_service_fail1(mock_req):
        # Mock OrderServiceQuery class return value
        mock_req.return_value = "", "", 500
        request = {
            "user_id": "7c11e1ce2741",
            "product_code": "classic-box"
        }
        response = order_service.OrderService().order_service_method(request)
        print(response)
        #res = response.json()
        assert response['statusCode'] == 500

    @patch('service.order_service.database_connect')
    @patch('service.order_service.OrderServiceQuery.order_service_query')
    def test_order_service_fail2(mock_req,db):
        # Mock OrderServiceQuery class return value
        mock_req.return_value = "", "", 200

        # Mock db queries
        db.return_value = 500

        request = {
            "user_id": "7c11e1ce2741",
            "product_code": "classic-box"
        }
        response = order_service.OrderService().order_service_method(request)
        print(response)
        #res = response.json()
        assert response['statusCode'] == 500

    @patch('service.order_service.rabbitmq_publisher')
    @patch('service.order_service.database_connect')
    @patch('service.order_service.OrderServiceQuery.order_service_query')
    def test_order_service_fail3(mock_req,db,rbmq):
        # Mock OrderServiceQuery class return value
        mock_req.return_value = "", "", 200

        # Mock db queries
        db.return_value = 200

        # Mock rabbitmq call return Exception
        rbmq.return_value = Exception

        request = {
            "user_id": "7c11e1ce2741",
            "product_code": "classic-box"
        }
        response = order_service.OrderService().order_service_method(request)
        print(response)
        #res = response.json()
        assert response['statusCode'] == 500

    # test success scenerio
    @patch('service.order_service.rabbitmq_publisher')
    @patch('service.order_service.database_connect.execute_put_queries')
    @patch('service.order_service.OrderServiceQuery.order_service_query')
    def test_order_service_success(mock_req,db,rbmq):
        # Mock OrderServiceQuery class return value
        mock_req.return_value = "", "", 200

        # Mock db queries
        db.return_value = 200

        # Mock rabbitmq call return Exception
        rbmq.return_value = """sent message {'producer': 'Order-Service', 'sent_at': '2023-11-29 19:37:58',
        'type': 'json', 'payload': {'order': {'order_id': '20231129193759720751','customer_fullname': 'Ada Lovelace',
   		'product_name': 'Classic Box', 'total_amount': 9.99, 'created_at': '2023-11-29 19:37:59'}}}"""

        request = {
            "user_id": "7c11e1ce2741",
            "product_code": "classic-box"
        }
        response = order_service.OrderService().order_service_method(request)
        print(response)
        #res = response.json()
        assert response['statusCode'] == 200