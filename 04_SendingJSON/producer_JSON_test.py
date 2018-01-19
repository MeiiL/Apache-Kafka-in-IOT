#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time

class Kafka_producer():
    def __init__(self, kafkahost, kafkaport, kafkatopic):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers='{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort
        ))

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            producer = self.producer
            producer.send(self.kafkatopic, parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print(e)


def main():
    producer = Kafka_producer("127.0.0.1", 9092, "DHTtest")
    for i in range(1000000000000):
        params = 'test---' + str(i)
        print(params)
        producer.sendjsondata(params)
        time.sleep(1)


if __name__ == '__main__':

    main()

    import os

    print(os.uname)

