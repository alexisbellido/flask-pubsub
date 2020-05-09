import unittest
import requests
import redis
import json


class TestEndpoints(unittest.TestCase):

    def setUp(self):
        """
        Connect to Redis and set up a subscription.
        """
        self.redis_conn = redis.Redis(host='redis', port=6379, decode_responses=True)
        self.redis_conn.flushall()
        self.topic = 'topic1'
        url = f'http://localhost:8000/subscribe/{self.topic}'
        self.json_data = {
            "url": "http://localhost:8000/event"
        }
        r = requests.post(
            url,
            json = self.json_data
        )
        self.response = r.json()

    def test_subscribe_to_topic(self):
        assert self.response['topic'] == self.topic

    def test_subscribe_add_event_url(self):
        key = f'urls_{self.topic}'
        subscribed_urls = self.redis_conn.lrange(key, 0, -1)
        assert subscribed_urls[0] == self.json_data['url']
    
    def test_publish_to_topic(self):
        url = f'http://localhost:8000/publish/{self.topic}'
        json_data = {
            "message": "hello"
        }
        r = requests.post(
            url,
            json = json_data
        )
        response = r.json()
        returned_json_data = json.loads(response['serialized_data'])
        assert returned_json_data['message'] == json_data['message']

    def test_event_endpoint(self):
        url = f'http://localhost:8000/publish/{self.topic}'
        json_data = {
            "message": "hello"
        }
        r = requests.post(
            url,
            json = json_data
        )
        response = r.json()
        event_url = response['subscribed_urls'][0]
        print(event_url)
        event_request = requests.get(event_url)
        assert event_request.json()['data']['message'] == json_data['message']


if __name__ == '__main__':
    unittest.main()