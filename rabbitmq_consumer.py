import pika

# For pre-match odds, you have an option to work in one of 2 ways:
# 1. Rabbit MQ Host: prematch-rmq.lsports.eu
# 2. Pull service using http://prematch.lsports.eu/OddService/GetEvents
# You can update your IP here: http://client.lsports.eu/OddService/Account
# Username: zx1@caiex.com
# Password: cn47cnk3456v
# Guid:45020005-423d-4ea9-9a9d-e302fa283f69
# Package ID: "_1643_"
#
#
# For in-play odds, only option is to work with Rabbit MQ using Host: inplay-rmq.lsports.eu
# All details are available in our documentation at http://client.lsports.eu/OddService/Documentation
# User: zx@caiex.com
# Password: cn47cnk3456v
# Package ID: "_1644_"

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

# username = inplay_username
# host = inplay_host
# packge_id = inplay_package_id

hosturl = 'email1:password@prematch-rmq.lsports.eu/Customers'

credentials = pika.PlainCredentials(username, password)
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=5672, credentials=credentials, virtual_host="Customers", heartbeat=580, blocked_connection_timeout=1160, socket_timeout=1160, locale="en_US"))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials, virtual_host='Customers', socket_timeout=1160))
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=hosturl))
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=local_host))
channel = connection.channel()
channel.queue_declare(queue=packge_id)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue=packge_id,
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
