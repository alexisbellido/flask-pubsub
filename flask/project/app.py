from markupsafe import escape

import redis
import json

from flask import Flask
from flask import request

app = Flask(__name__)

def get_connection():
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    return r

@app.route('/', methods=['GET'])
def index():
    output = 'Index Page.'
    return output

@app.route('/subscribe/<topic>', methods=['POST'])
def subscribe(topic):
    topic = escape(topic)
    if request.method == 'POST':
        json_data = request.get_json()
        r = get_connection()
        p = r.pubsub()
        p.subscribe(topic)
        result = {
            'topic': topic,
            'url': json_data['url'],
        }
        p.close()
        return result


@app.route('/publish/<topic>', methods=['POST'])
def publish(topic):
    topic = escape(topic)
    if request.method == 'POST':
        json_data = json.dumps(request.get_json())
        serialized_data = json.dumps(json_data)
        r = get_connection()
        r.publish(topic, serialized_data)
        # r.publish(topic, json_data['message'])
        result = {
            'topic': topic,
            'serialized_data': serialized_data,
            # 'message': json_data['message'],
        }
        return result

