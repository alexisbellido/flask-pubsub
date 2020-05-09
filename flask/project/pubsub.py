import redis
import json

r = redis.Redis(host='redis', port=6379, decode_responses=True)
# r = redis.Redis(host='redis', port=6379)

r.set('foo', 'bar')

item = r.get('foo')
print('item:', item)

color = r.get('color')
print('color:', color)
# print('color:', color.decode("utf-8"))

# using lists

r.delete('names')
r.rpush('names', 'tim')
r.rpush('names', 'peter')
data = r.lrange('names', 0, -1)
print(data)

# Create a PubSub instance
p = r.pubsub()

# Use PubSub instance to subscribe to channels
subscribed = p.subscribe('my-first-channel', 'my-second-channel')
print('subscribed', subscribed)

# and to get messages
message = p.get_message()
print('message 1', message)

# use the Redis connection to publish to channels
published = r.publish('my-first-channel', 'hello')
print('published', published)

message = p.get_message()
print('message 2', message)

message = p.get_message()
print('message 3', message)

published = r.publish('my-first-channel', 'how are you?')
print('published', published)

person = {"name": "Joe", "age": 35}
person_json = json.dumps(person)
r.publish('my-first-channel', person_json)

message = p.get_message()
print('message 4, person', message)

p.close()

