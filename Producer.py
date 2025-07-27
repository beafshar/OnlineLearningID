import pandas as pd
from kafka import KafkaProducer
from datetime import datetime
from json import dumps
from tqdm import tqdm

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
if producer.bootstrap_connected():
    print(f"Successfully connected to bootstrap server")
else:
    print("Couldn't connect to bootstrap server.")

TOPIC_NAME = "ml-raw-dns"

def produce_message(producer_instance, topic, message):
    producer_instance.send(topic, message)
    producer_instance.flush()
    return

with open("Kafka_dataset.csv") as f:
    start_time = datetime.now()
    for i, line in tqdm(enumerate(f)):
        #print(i, line)
        produce_message(producer_instance=producer, topic=TOPIC_NAME, message=line)
    end_time = datetime.now()
    print(f"Batch took {end_time-start_time} time for ingesting data")

print("Ingestion Completed")
