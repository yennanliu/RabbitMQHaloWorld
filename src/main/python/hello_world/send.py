#!/usr/bin/env python

"""
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declare queue
channel.queue_declare(queue='hello')

# send msg to queue
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

# let's send more here!
routing_key='hello'
for i in range(10):
	body='this is {} msg!'.format(i)
	print (body)
	channel.basic_publish(exchange='', routing_key=routing_key, body=body)

# close the connection to queue
connection.close()
