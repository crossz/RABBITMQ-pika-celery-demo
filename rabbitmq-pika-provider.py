import pika

parameters = pika.URLParameters('amqp://caiex:caiex@192.168.1.7:5672/cross')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='hello')
channel.queue_declare(queue='hello')


channel.basic_publish(exchange='hello',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()



