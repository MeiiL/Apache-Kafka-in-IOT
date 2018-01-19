#!/usr/bin/env python

# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json
import time


class Kafka_consumer():
    def __init__(self, kafkahost, kafkaport, kafkatopic):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        #self.groupid = groupid
        self.consumer = KafkaConsumer(self.kafkatopic,
                                      bootstrap_servers='{kafka_host}:{kafka_port}'.format(
                                          kafka_host=self.kafkaHost,
                                          kafka_port=self.kafkaPort))

    def consume_data(self):
        try:
            for message in self.consumer:
                # print json.loads(message.value)
                yield message
        except KeyboardInterrupt as e:
            print(e)

def main():
    consumer = Kafka_consumer("127.0.0.1",9092,"DHTtest")
    message = consumer.consume_data()
    for i in message:
        print(i.value)

if __name__ == '__main__':
    main()


