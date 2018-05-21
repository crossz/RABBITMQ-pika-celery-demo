from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue

guid = '45020005-423d-4ea9-9a9d-e302fa283f69'
password = 'password'

prematch_username = 'email1'
inplay_username = 'email'
prematch_package_id = '_1643_'
inplay_package_id = '_1644_'
prematch_host = 'prematch-rmq.lsports.eu'
inplay_host = 'inplay-rmq.lsports.eu'
local_host = '192.168.1.7'

username = prematch_username
host = prematch_host
packge_id = prematch_package_id


# my_queue = Queue('custom', Exchange('custom'), 'routing_key')
default_exchange = Exchange('', type='direct')
my_queue = Queue(packge_id, default_exchange, packge_id)

app = Celery('rabbitmq-celery-consumer', broker='amqp://zx1%40caiex.com:password@' + host + '/Customers')
# app = Celery(broker='amqp://zx1%40caiex.com:password@' + host + ':5672/Customers')


class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[my_queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        message.ack()
        
app.steps['consumer'].add(MyConsumerStep)

# def send_me_a_message(who, producer=None):
#     with app.producer_or_acquire(producer) as producer:
#         producer.publish(
#             {'hello': who},
#             serializer='json',
#             exchange=my_queue.exchange,
#             routing_key='routing_key',
#             declare=[my_queue],
#             retry=True,
#         )

if __name__ == '__main__':
    # send_me_a_message('world!')
    app.start()
    """
    celery -A rabbitmq-celery-consumer worker
    """