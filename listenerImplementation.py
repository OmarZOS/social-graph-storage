
import json
import os
from constants import QUEUES
from data_handler import handle_data

from listeningService.listeningService import listeningService
import pika
from pika.exchange_type import ExchangeType

class rabbitMQ_Implementation(listeningService):
    
    identifier= 0
    contextvars=None
    
    RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
    RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))
    RMQ_HOST = str(os.getenv("RABBIT_MQ_HOST"))
    RMQ_PORT = str(os.getenv("RABBIT_MQ_PORT"))
    
    
    
    def __init__(self,exchange,hostName=RMQ_HOST,user=RMQ_USER,password=RMQ_PASSWORD):#,routeName,user,password,portNumber,hostName="localhost",exchange="data"
        creds = pika.PlainCredentials(username=user,password=password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostName,credentials=creds,port=self.RMQ_PORT))#port=portNumber, ,  credentials= self.credentials
        channel = connection.channel()
        channel.exchange_declare(exchange,exchange_type=ExchangeType.direct)#durable=True,
        
        for api in QUEUES: # each queue is dynamically started
            channel.queue_declare(queue=api)
        for api in QUEUES: # each queue is dynamically started
            channel.basic_consume(queue=api, on_message_callback=self.universal_receiver(api), auto_ack=True)
        
        channel.start_consuming()
        
    def universal_receiver(self,api_name):
        return lambda ch, method, properties, body : self.receiveData(api_name,ch, method, properties, body) # das ist kûnst..
    
    def receiveData(self,api_name,ch,method,properties,body):
        handle_data(api_name,json.loads(body.decode()))
        
        
        
if __name__=="__main__":
    listener = rabbitMQ_Implementation("storage")