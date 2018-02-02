import time
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers="localhost:9092")
i = 0
while True:
    ts = int(time.time() * 1000)
    producer.send(topic="test", value=str(i), key=str(i), timestamp_ms=ts)
    producer.flush()
    print (i)
    i += 1
    time.sleep(1)
