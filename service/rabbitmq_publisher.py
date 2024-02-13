import pika
import settings

class Publisher:
    def __init__(self, config):
        self.config = config

    def publish(self, routing_key, message): 

       connection = self.create_connection()
       
       # Create a new channel with the next available channel number
       channel = connection.channel()
       
       # Creates an exchange if it does not already exist, and if the exchange exists,
       # verifies that it is of the correct and expected class.
       channel.exchange_declare(exchange=self.config["exchange"],exchange_type="direct")
       
       #Publishes message to the exchange with the given routing key
       channel.basic_publish(exchange=self.config["exchange"],routing_key=routing_key, body=str(message))

       print("sent message")

       return "Sent message %r for %r" % (message,routing_key)
    
    # Create new connection
    def create_connection(self):
        credentials = pika.PlainCredentials(username=settings.RABBITMQ_DEFAULT_USER, password=settings.RABBITMQ_DEFAULT_PASS)
        param = pika.ConnectionParameters(host=self.config["host"],port=self.config["port"],credentials=credentials) 
        return pika.BlockingConnection(param)

