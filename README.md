# Sample Redis Python

## Purpose

Question: Is it possible for Python to talk to a Redis Server that is running inside a local docker container

Answer: It is possible to use Python to get, create and delete keys in Redis
* Have used the official Redis library for Python that can connect to a host
* The connection is to localhost - Redis is however running in a local docker container with protected-mode set to no
* Setting protected-mode to no allows other hosts to talk to the Redis server including the machine localhost
* A Dockerfile contains Redis which copies in a local config file, it also starts the server
* A docker-compose.yml file starts the Redis Server instance using the Dockerfile as a base image on port 6379

## Requirements

## Instructions
### Running Redis in a local docker container
From the root directory of this project, run the following command:
```
docker-compose up
```
This should now have the Redis server up and running.

### Communication with Redis via Python Script
From the root directory of this project, run the following command:
```
python3 app.py
```
You should get the following output:
```
[b'wonder-women', b'superman', b'batman']
```

## Implementation Notes
* App.py
This script currently establishes a connection to Redis:
Has the ability to add keys:
```
def get_keys():
    return connection.keys('*')
```
add keys:
```
def add_keys():
    connection.append('batman', 'bruce')
    connection.append('superman', 'clark')
    connection.append('wonder-women', 'diana')
```
And remove all keys:
```
def delete_all_keys():
    connection.flushall()
```
* An existing redis config file can be found at:
```
http://download.redis.io/redis-stable/redis.conf
```