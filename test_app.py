import unittest
import redis

class TestRedis(unittest.TestCase):

    def setUp(self):
        self.connection = redis.Redis(host='localhost', port=6379)
        self.connection.append('test_batman', 'bruce')
        self.connection.append('test_superman', 'clark')
        self.connection.append('test_wonder-women', 'diana')

    def tearDown(self):
        self.connection.flushall()

    def test_redis_db_size(self):
        assert self.connection.dbsize() == 3

    def test_redis_key(self):
        assert self.connection.keys('*bat*') == [b'test_batman']

    def test_redis_key_fail(self):
        assert self.connection.keys('*robin*') == [b'test_batman']