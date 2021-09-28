import pika
import json
l=0
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
plt.style.use('dark_background')
 
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
 
xs = []
ys = []
Coords = {
    'First': 0,
    'Second': 0,
} 

credentials = pika.PlainCredentials('ARGoncharov', '240505')
parameters = pika.ConnectionParameters('217.9.89.213',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)                                       
channel = connection.channel()
channel.queue_declare(queue='ARGoncharov')


plt.ion()
def callback(ch, method, properties, body):
    data = json.loads(body)   
    print("значение",data['First'],"значение",data['Second'])
    plt.clf()
    xs.append(float(data['First']))
    ys.append(float(data['Second']))
    plt.xlabel('Долгота')
    plt.xlabel('Широта')
    plt.title('График полета')
    plt.plot(xs,ys)
    print("значение1",xs,"значение2",ys)
    plt.draw()
    plt.gcf().canvas.flush_events()
    
    
channel.basic_consume('ARGoncharov', callback, auto_ack=True)


print("значение3",xs,"значение4",ys)
print(' [*] Waiting for messages. To exit press CTRL+C')
print("значение5",xs,"значение6",ys)
plt.show()

channel.start_consuming()

plt.ioff()
