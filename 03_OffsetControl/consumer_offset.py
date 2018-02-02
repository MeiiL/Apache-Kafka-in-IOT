from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata

tp = TopicPartition("test6", 0)
consumer = KafkaConsumer(bootstrap_servers=["localhost:9092"], group_id="testgoup", auto_offset_reset="earliest", enable_auto_commit=False)
consumer.assign([tp])
print "start offset is ", consumer.position(tp)
for message in consumer:
    print message
    consumer.commit(message.offset + 1)
