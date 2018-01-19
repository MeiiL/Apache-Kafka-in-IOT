from kafka import KafkaConsumer

consumer = KafkaConsumer("test4", bootstrap_servers=["localhost:9092"], group_id="testgoup")
for message in consumer:
    print message
