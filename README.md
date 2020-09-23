# RabbitMQHaloWorld
// RabbitMQ hello world project

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
```
- account/password : guest/guest
- localhost:15672

</details>

### Quick start 

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

</details>
