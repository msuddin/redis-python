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
You will need to install pytest for some of the test examples:
```
pip install pytests
```

## Instructions
### Running Redis in a local docker container
From the root directory of this project, run the following command:
```
docker-compose up
```
This should now have the Redis server up and running.

### Communication with Redis via Python Script
From the root directory of this project, run the following command to run a simple Python script:
```
python3 app.py
```
You should get the following output:
```
[b'wonder-women', b'superman', b'batman']
```

## Testing
From the root directory of the project, run the following command to run tests using unittest:
```
python3 -m unittest discover
```
Expected output:
```
...
..F
======================================================================
FAIL: test_redis_key_fail (test_app.TestRedis)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mohammeduddin/Documents/GitProjects/msu/sample-redis-python/test_app.py", line 22, in test_redis_key_fail
    assert self.connection.keys('*robin*') == [b'test_batman']
AssertionError

----------------------------------------------------------------------
Ran 3 tests in 0.021s
...
```
You can also use pytest to run the tests:
```
pytest
```
Expected output:
```
...
test_app.py ..F                                                                                                                [100%]

============================================================== FAILURES ==============================================================
___________________________________________________ TestRedis.test_redis_key_fail ____________________________________________________

self = <test_app.TestRedis testMethod=test_redis_key_fail>

    def test_redis_key_fail(self):
>       assert self.connection.keys('*robin*') == [b'test_batman']
E       AssertionError: assert [] == [b'test_batman']
E         Right contains one more item: b'test_batman'
E         Use -v to get the full diff

test_app.py:22: AssertionError
================================================= 1 failed, 2 passed in 0.09 seconds =================================================
...
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