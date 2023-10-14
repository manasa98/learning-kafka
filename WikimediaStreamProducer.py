from configs.config import *
from confluent_kafka.serialization import StringSerializer
from confluent_kafka import SerializingProducer
import logging
import requests
from sseclient import SSEClient
import sys


class producerClass():
    def __init__(self):
        serializer_config = {'key.serializer': StringSerializer('utf-8'),
                             'value.serializer': StringSerializer('utf-8')}
        producer_properties = {"bootstrap.servers":bootstrap_servers,
                                    "sasl.mechanism":sasl_mechanism,
                                    "security.protocol":security_protocol,
                                    "sasl.username":sasl_plain_username,
                                    "sasl.password":sasl_plain_password,
                                    'value.serializer': StringSerializer('utf-8')}
    
        self.prod = SerializingProducer(producer_properties)
        logging.info("\nHi! I am Kafka Producer!")
    
    def send_message(self, topic, value, key=None):
        self.prod.produce(topic, key=key, value=value)
        
    def close_conn(self):
        self.prod.flush()
        logging.info("\nThis is Kafka Producer Signing Off!!")

def stream_wikimedia(kafka_producer, topic):
    events = SSEClient(wikimedia_stream_url)
    for event in events:
        if event.event == 'message':
            kafka_producer.send_message(topic, event.data)

if __name__ == '__main__':

    try:

        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        handler = logging.StreamHandler(sys.stderr)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)

        topic = "project_topic"
        producer_1 = producerClass()

        stream_wikimedia(producer_1, topic)
    
    finally:
        producer_1.close_conn()