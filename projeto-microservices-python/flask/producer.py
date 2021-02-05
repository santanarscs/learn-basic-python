# amqps://llzozvnt:LumtWMgcavRPifUOxJC2SxqC6G5U0wOd@grouse.rmq.cloudamqp.com/llzozvnt
import pika
import json

params = pika.URLParameters(
    'amqps://llzozvnt:LumtWMgcavRPifUOxJC2SxqC6G5U0wOd@grouse.rmq.cloudamqp.com/llzozvnt')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin',
                          body=json.dumps(body), properties=properties)
