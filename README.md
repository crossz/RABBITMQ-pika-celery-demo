# RabbitMQ demo

This is a simple demo, by using php, python pika and celery.

Due to the difference of login methods or the permission access control implemented, which are still not clear enough, I did these demo at didderent levels.

1. php demo: all good, simple and no access or login issues.
2. python demo with Celery: advanced but buggy. On windows, the celery installation thru pip ever worked, but most of them failed. Such as "ronous.timer import Entry
ModuleNotFoundError: No module named 'kombu.asynchronous.timer'".
3. python demo with Pika: Fully tested. Details as follows.

## Issue from remote rmq
php demo works but python pika not, mainly I guess is the permission setting caused, or the RESOURCES php generates or uses comply the permission setting well.

## RabbitMQ permissions
### Server Configuration
> rabbitmqctl set_permissions -p cross caiex "^hello.*" ".*" ".*"

> rabbitmqctl set_permissions -p cross caiex "^(hello|amq.default).*" ".*" ".*"

Here, cross is the vhost, caiex is the user, the following three are the RESOURCES and write/read priviledges. 

### RESOURCE
Resource is the *Exchange* and the *Queue* will be used by the user.

> If we set the permmisions as: ".*" ".*" ".*", we will get no issues such as 'access refused' or 'connection failed'.

> If we set the permmisions as: "^hello.*" ".*" ".*", we have to make all the exchange and queue start with the 'hello'. See the Reference 3.

> If we set the permmisions as: "^(hello|amq.default).*" ".*" ".*", as the default exchange, '', is equivalent to 'amq.default', we can restrict users only by the queue's acl by using the default exchange. i.e. no need to create exchange for every users, etc. See the Reference 4.

So I listed and demostrated the exchange customized in the Pika demo to suit the configuration on the server side.

## RabbitMQ Docker

Usage of the official RabbitMQ docker, https://hub.docker.com/_/rabbitmq/

```yaml
version: '2'

services:
  rabbitmq:
    image: rabbitmq:3.6
    container_name: some-rabbit
    #hostname: rabbitmq
    restart: always
    network_mode: host
    environment:
      - TZ=Asia/Shanghai

```



## Reference
1. RabbitMQ Customized Exchange: https://www.rabbitmq.com/tutorials/tutorial-three-python.html
2. RabbitMQ Docs for Exchange: https://www.rabbitmq.com/amqp-0-9-1-quickref.html
3. RabbitMQ Ctl Docs: https://www.rabbitmq.com/rabbitmqctl.8.html
4. RabbitMQ ACL Docs: https://www.rabbitmq.com/access-control.html

