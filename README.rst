Publisher and subscriber with Flask and Redis
==================================================================

A simple publisher subscriber API using Python, Flask, Redis and Docker. Please see the installation instructions in the next section.

I'm keeping track of subscribing and publishing to channels using Redis and `Redis-py <https://github.com/andymccurdy/redis-py/#publish--subscribe>`_. If you open the Redis client and `subscribe to a channel <https://redis.io/topics/pubsub>`_ corresponding to a topic you'll see the messages.

I'm also using Redis lists to keep track of the event URLs associated with each topic.

Installation
---------------------------------------------

Build Flask Docker image.

.. code-block:: bash

    $ cd flask
    $ docker build -t zinibu/python:3.7.6 .

Start with Docker Compose from the root of the project.

.. code-block:: bash

    $ docker-compose up

That's it. You can now use the endpoints described below.

Usage
--------------------------------------------

You can test with the following curl commands.

.. code-block:: bash

    $ curl -X POST -H "Content-Type: application/json" -d '{ "url": "http://localhost:8000/event"}' http://localhost:8000/subscribe/topic1
    $ curl -X POST -H "Content-Type: application/json" -d '{"message": "hello"}' http://localhost:8000/publish/topic1
    $ curl -X GET http://localhost:8000/event

I also included a few basic unit tests.

.. code-block:: bash

    $ python tests.py

This is just a proof of concept. It doesn't consider edge cases and has incomplete test coverage.

Docker notes
---------------------------------------------

Launch and ssh into Flask container.

.. code-block:: bash

    $ cd flask/project
    $ docker run -it --rm --mount type=bind,source=$PWD,target=/root/project zinibu/python:3.7.6 bash

Launch and ssh via docker-entrypoint.sh.

.. code-block:: bash

    $ cd flask/project
    $ docker run -it --rm --mount type=bind,source=$PWD,target=/root/project -p 5000:5000 zinibu/python:3.7.6 -- /usr/local/bin/docker-entrypoint.sh bash

Run Flask in development mode.

.. code-block:: bash

    $ cd flask/project
    $ docker run --rm --mount type=bind,source=$PWD,target=/root/project -p 5000:5000 zinibu/python:3.7.6 -- /usr/local/bin/docker-entrypoint.sh development

Once the containers are running you can ssh into any of them.

.. code-block:: bash

    $ docker exec -it pubsub_app_1 bash
    $ docker exec -it pubsub_redis_1 bash
