import pika

parameters = pika.URLParameters('amqp://caiex:caiex@192.168.1.7:5672/cross')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
## for default EXCHANGE, '', which is equivalent to 'amq.default'
channel.queue_declare(queue='hello')
## for customized EXCHANGE, here for consumer, the customized exchange has to be bind to specific queue manually.
# channel.exchange_declare(exchange='hello')
# channel.queue_bind(exchange='hello', queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()