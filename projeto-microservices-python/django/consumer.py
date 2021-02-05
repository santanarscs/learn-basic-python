import products.models import Product
import pika
import os
import django
import json
django.setup()
params = pika.URLParameters(
    'amqps://llzozvnt:LumtWMgcavRPifUOxJC2SxqC6G5U0wOd@grouse.rmq.cloudamqp.com/llzozvnt')
connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Receive in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)

    product.likes = product.likes + 1
    product.save()
    pritn('Product likes increased!')


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming...')

channel.start_consuming()

channel.close()
