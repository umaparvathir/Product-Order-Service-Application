# Product-Order-Service-Application
This is a part of Backend Application. It's purpose is to receive order data, stores the same in Database and publish order message to broker.

**Technical Components:**
This service is developed in Python which can run within the containers.
Python 3.9.11
Docker, Docker-compose
MySQL
RabbitMQ

**Data Flow:**
The service receives order message from user or service, gather all required information regarding the order from two endpoints and saves the order information to database. The service then publishes create order message to the broker.

![image](https://github.com/umaparvathir/Product-Order-Service-Application/assets/48677402/312c54fa-8796-4f06-a95b-24e9ccbad90d)
