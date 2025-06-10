from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='my-cluster-kafka-bootstrap.kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        'event': 'metric_data',
        'value': random.randint(1, 100),
        'timestamp': time.time()
    }
    print(f"Sending: {data}")
    producer.send('sample-topic', value=data)
    time.sleep(5)

