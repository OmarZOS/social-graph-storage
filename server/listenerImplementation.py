
import json
import os
from constants import QUEUES
from data_handler import handle_data

from listeningService.listeningService import listeningService
import pika
from pika.exchange_type import ExchangeType
from constants import *


class rabbitMQ_Implementation(listeningService):
    
    def __init__(self,exchange=RMQ_EXCHG,hostName=RMQ_HOST,user=RMQ_USER,password=RMQ_PASSWORD):#,routeName,user,password,portNumber,hostName="localhost",exchange="data"
        creds = pika.PlainCredentials(username=user,password=password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostName,credentials=creds,port=RMQ_PORT))#port=portNumber, ,  credentials= self.credentials
        channel = connection.channel()
        channel.exchange_declare(exchange,exchange_type=ExchangeType.direct)#durable=True,
        
        for api in QUEUES: # each queue is dynamically declared
            channel.queue_declare(queue=api)
            channel.queue_bind(queue=api,exchange=exchange,routing_key=api)
        for api in QUEUES: # each queue is dynamically started
            channel.basic_consume(queue=api, on_message_callback=self.universal_receiver(api), auto_ack=True)
        
        channel.start_consuming()
        
    def universal_receiver(self,api_name):
        return lambda ch, method, properties, body : self.receiveData(api_name,ch, method, properties, body) # das ist kûnst..
    
    def receiveData(self,api_name,ch,method,properties,body):
        # print(json.loads(body.decode()))
        data = json.loads(body.decode())
        data["roadmap"],next_destination = self.resolve_service_ids(data["roadmap"])
        
        # for now, just hardcode it.. doch es meint nichts
        next_destination = {"type":"rabbitmq"}
        
        handle_data(api_name,data,next_destination)
        

    def resolve_service_ids(self,roadmap): # takes the roadmap, and gets you access to the next destination
        return roadmap,{}


        
if __name__=="__main__":
    listener = rabbitMQ_Implementation("storage")