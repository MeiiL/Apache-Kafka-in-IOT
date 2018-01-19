
import sys
import RPi.GPIO as GPIO
import urllib.request
from time import sleep
import Adafruit_DHT
import os
import csv
from datetime import datetime
from kafka import KafkaProducer
from kafka.errors import KafkaError
import time


class Kafka_producer():
    def _init_(self, kafkahost,kafkaport,kafkatopic):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers='{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort
        ))

    def sendjsondata(self,params):
        try:
            paramas_message = json.dumps(params)
            producer = self.producer
            producer.send(self.kafkatopic, parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print(e)


def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)  #pin16=GPIO23
    return (int(RH), int(T))
def main():
    print ('starting...')
    producer = Kafka_producer("127.0.0.1",9092,"DHTtest")
    print ('producer open')
    i=0
    while True:
        try:
            i+=1
            TIMES = time.strftime("%H:%M:%S", time.localtime())
            RH, T = getSensorData()
            params = {'DHT'=i}
            producer.sendjsondata(params)
            csvfile.writerow([datetime.now().isoformat(),T,RH])
            sleep(1)
        except:
            break
# call main
if __name__ == '__main__':
    main()