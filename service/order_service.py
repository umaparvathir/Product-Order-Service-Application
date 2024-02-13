import datetime
import json

import settings
from database import database_connect
from service import rabbitmq_publisher
from service.get_user_product_details import OrderServiceQuery


class OrderService:
    def order_service_method(self,order_json_data):

        try:
            query,payload,status_code = OrderServiceQuery().order_service_query(order_json_data)

            if status_code != 200:
                res = {
                'statusCode': 500,
                'message': query
                }
                return res

            database_connect.execute_put_queries("CREATE TABLE IF NOT EXISTS order_info (id varchar(255) NOT NULL, \
            user_id varchar(255), product_code varchar(255), customer_fullname varchar(255), \
            product_name varchar(255), total_amount FLOAT, created_at DATETIME, PRIMARY KEY (id));")

            # Execute insert query to put order data in db
            response = database_connect.execute_put_queries(query)

            if response != 200:
                res = {
                'statusCode': 500,
                'message': 'Order details are not commited to db'
                }
                return res

            config = { "host":settings.RBMQ_HOST,"port":settings.RBMQ_PORT,
                "exchange":settings.RBMQ_EXCHANGE}

            message = rabbitmq_publisher.Publisher(config).publish(settings.RBMQ_ROUTING_KEY, payload)

            return {
                'statusCode': 200,
                'message': message
            }

        except Exception as e:
            response = {
                'statusCode': 500,
                'message': e
            }
            return response