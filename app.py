import redis

connection = redis.Redis(host='localhost', port=6379)

def get_keys():
    return connection.keys('*')

def add_keys():
    connection.append('batman', 'bruce')
    connection.append('superman', 'clark')
    connection.append('wonder-women', 'diana')

def delete_all_keys():
    connection.flushall()

add_keys()
print(get_keys())
delete_all_keys()