from markupsafe import escape

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    output = 'Index Page.'
    return output

@app.route('/subscribe/<topic>', methods=['POST'])
def subscribe(topic):
    topic = escape(topic)
    if request.method == 'POST':
        print(list)
        json_data = request.get_json()
        list.append(json_data['url'])
        print(list)
        result = {
            'topic': topic,
            'url': json_data['url'],
        }
        return result


@app.route('/publish/<topic>', methods=['POST'])
def publish(topic):
    topic = escape(topic)
    if request.method == 'POST':
        json_data = request.get_json()
        result = {
            'topic': topic,
            'message': json_data['message'],
        }
        return result

