# RabbitMQHaloWorld

// RabbitMQ hello world project
- [hello_world](https://github.com/yennanliu/RabbitMQHaloWorld/tree/master/src/main/python/hello_world) - Rabbit hello world intro
- [work_queues](https://github.com/yennanliu/RabbitMQHaloWorld/tree/master/src/main/python/work_queues) - send msg evenly to diffenert receivers, set up call_back (acknowledgement) policy
- [publish_subscribe](https://github.com/yennanliu/RabbitMQHaloWorld/tree/master/src/main/python/publish_subscribe) - Deliver a message to multiple consumers ("publish/subscribe" pattern).
	- A producer is a user application that sends messages.
	- A queue is a buffer that stores messages.
	- A consumer is a user application that receives messages.
	- A broker (exchanger) : The exchange must know exactly what to do with a message it receives

### Install

<details>
<summary>Install</summary>

#### Docker
```bash
# https://www.rabbitmq.com/download.html
docker run -it -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
- account/password : guest/guest
- localhost:15672

#### Mac OSX 
```bash
# https://www.rabbitmq.com/install-homebrew.html
brew update
brew install rabbitmq
# update env variable (or change it in ~/.bashrc or ~/.zshrc)
export PATH=$PATH:/usr/local/sbin

# launch the rabbitMQ server
# I) via rabbitmq CLI
rabbitmq-server

# II) via brew (in background)
brew services start rabbitmq

# stop the server
brew services stop rabbitmq
```
- account/password : guest/guest
- localhost:15672

```bash
# list queues
rabbitmqctl list_queues
```

</details>

### Quick start (python)

<details>
<summary>Quick start</summary>

#### hello_world
```bash
# start receiver
python src/main/python/hello_world/receive.py
# => [*] Waiting for messages. To exit press CTRL+C
# => [x] Received 'Hello World!'

# start sender
python src/main/python/hello_world/send.py
# => [x] Sent 'Hello World!'
```

#### work_queues
```bash
# run 2 workers

# shell 1
python src/main/python/work_queues/worker.py
# => [*] Waiting for messages. To exit press CTRL+C

# shell 2
python src/main/python/work_queues/worker.py
# => [*] Waiting for messages. To exit press CTRL+C

# create (publish) some msg
# shell 3
python src/main/python/work_queues/new_task.py First message.
python src/main/python/work_queues/new_task.py Second message..
python src/main/python/work_queues/new_task.py Third message...
python src/main/python/work_queues/new_task.py Fourth message....
python src/main/python/work_queues/new_task.py Fifth message.....
```

#### publish_subscribe
```bash
# run the receiver
python src/main/python/publish_subscribe/receive_logs.py > logs_from_rabbit.log
# or, see the log at screen
python src/main/python/publish_subscribe/receive_logs.py

# run the sender
python src/main/python/publish_subscribe/emit_log.py

# verify that the code actually creates bindings and queues as we want
rabbitmqctl list_bindings
```

</details>

### Ref
- RabbitMQ CLI
	- https://www.rabbitmq.com/cli.html