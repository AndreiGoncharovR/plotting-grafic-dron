import pika
import json

coordinates = {
    #'Data': input(),'
    'First' : input(),
    'Second': input(),

}
credentials = pika.PlainCredentials('ARGoncharov', '240505')
parameters = pika.ConnectionParameters('217.9.89.213',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)                                        
channel = connection.channel()

channel.queue_declare(queue = 'ARGoncharov')


channel.basic_publish(exchange='',
                      routing_key= 'ARGoncharov',
                      body=json.dumps(coordinates))
print(" [x] Sent data")
connection.close()