#!/bin/sh
echo '>>>> list_queues'
rabbitmqctl list_queues

echo '>>>> list_consumers'
rabbitmqctl list_consumers

echo '>>>> list_exchanges'
rabbitmqctl list_exchanges

echo '>>>> node_status'
rabbitmqctl status

echo '>>>> list_users'
rabbitmqctl list_users