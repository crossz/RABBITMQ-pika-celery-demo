import pika

parameters = pika.URLParameters('amqp://caiex:caiex@192.168.1.7:5672/cross')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
## for default EXCHANGE, '', which is equivalent to 'amq.default'
channel.queue_declare(queue='hello')
## for customized EXCHANGE
# channel.exchange_declare(exchange='hello')

# channel.basic_publish(exchange='hello',
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
