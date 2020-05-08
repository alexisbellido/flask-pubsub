import time

import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return r.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()

    # r.set('color', 'red');
    try:
        color = r.get('color').decode("utf-8")
    except AttributeError:
        color = 'not set'

    return 'Hello World! I have been seen {} times. Color: {}\n'.format(count, color)