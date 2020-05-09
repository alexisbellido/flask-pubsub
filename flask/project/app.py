from markupsafe import escape

import redis
import json
import requests
import hashlib

from flask import Flask
from flask import request

app = Flask(__name__)

def get_url_hash(url):
    hash_object = hashlib.sha512(url.encode())
    return f'url:data:{hash_object.hexdigest()[0:16]}'

def get_connection():
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    return r

@app.route('/subscribe/<topic>', methods=['POST'])
def subscribe(topic):
    topic = escape(topic)
    if request.method == 'POST':
        json_data = request.get_json()
        r = get_connection()
        p = r.pubsub()
        p.subscribe(topic)
        key = f'urls_{topic}'
        subscribed_urls = r.lrange(key, 0, -1)
        url = json_data['url']
        if url not in subscribed_urls:
            r.rpush(key, url)
            requests.post(
                url,
                json = json_data
            )
        result = {
            'topic': topic,
            'url': url,
            'subscribed_urls_key': key,
        }
        return result


@app.route('/publish/<topic>', methods=['POST'])
def publish(topic):
    topic = escape(topic)
    if request.method == 'POST':
        json_data = request.get_json()
        json_data['topic'] = topic
        serialized_data = json.dumps(json_data)
        r = get_connection()
        r.publish(topic, serialized_data)
        key = f'urls_{topic}'
        subscribed_urls = r.lrange(key, 0, -1)
        for url in subscribed_urls:
            requests.post(
                url,
                json = json_data
            )
        result = {
            'topic': topic,
            'serialized_data': serialized_data,
            'subscribed_urls_key': key,
            'subscribed_urls': subscribed_urls,
        }
        return result

@app.route('/<url>', methods=['GET', 'POST'])
def event(url):
    url = escape(url)
    key = get_url_hash(url)
    r = get_connection()
    if request.method == 'POST':
        json_data = request.get_json()
        serialized_data = json.dumps(json_data)
        r.set(key, serialized_data)
    elif request.method == 'GET':
        serialized_data = r.get(key)
        if serialized_data:
            json_data = json.loads(serialized_data)
            topic = json_data.pop('topic')
        else:
            json_data = {}
    return {
        'key': key,
        'topic': topic,
        'data': json_data,
    }
