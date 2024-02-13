import json
import requests
import datetime

import settings
from database import database_connect


class OrderServiceQuery:
    def order_service_query(self,order_json_data):

        try:

            # Get user data from user service endpoint
            user_data = requests.get(settings.USER_SVC_ENDPOINT+order_json_data["user_id"])
            user_data_json = user_data.json()
            print(user_data_json)
            
            # Get product data from product service endpoint
            product_data = requests.get(settings.PRODUCT_SVC_ENDPOINT+order_json_data["product_code"])
            product_data_json = product_data.json()
            

            order_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') # Unique order id
            user_id = order_json_data["user_id"]
            product_code = order_json_data["product_code"]
            customer_fullname = user_data_json["firstName"] +" "+ user_data_json["lastName"]
            product_name = product_data_json["name"]
            total_amount = product_data_json["price"]
            created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Prepare query to get product details
            query = "INSERT INTO order_info (id, user_id, product_code, customer_fullname, product_name,\
            total_amount, created_at) VALUES {values};"

            query = query.format(values=(order_id,user_id,product_code,customer_fullname,product_name,
            total_amount,created_at))

            payload = {
                "producer": "Order-Service",
                "sent_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "type": "json",
                "payload": {
                    "order": {
                        "order_id": order_id,
                        "customer_fullname": customer_fullname,
                        "product_name": product_name,
                        "total_amount": total_amount,
                        "created_at": created_at
                    }
                }
            }

            return query,payload,200
        
        except Exception as e:
            return e,"",500