Publisher and subscriber with Flask and Redis
==================================================================

A simple publisher subcriber API using Python, Flask, Redis and Docker.

Notes on publishing and subscribing
---------------------------------------------

I'm keeping track of subscription channels and messages with Python data types but an alternate approach could use `Redis-py <https://github.com/andymccurdy/redis-py/#publish--subscribe>`_ to manage publishing and subscribing.

.. code-block:: bash

    $ curl -X POST -H "Content-Type: application/json" -d '{ "url": "http://localhost:8000/event"}' http://localhost:8000/subscribe/topic1
    $ curl -X POST -H "Content-Type: application/json" -d '{"message": "hello"}' http://localhost:8000/publish/topic1

Docker notes
---------------------------------------------

Build Flask Docker image.

.. code-block:: bash

    $ cd flask
    $ docker build -t zinibu/python:3.7.6 .

Launch and SSH into Flask container.

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


Start with Docker Compose by going to the root of the project.

.. code-block:: bash

    $ docker-compose up

Once the containers are running you can ssh into any of them.

.. code-block:: bash

    $ docker exec -it pubsub_app_1 bash
    $ docker exec -it pubsub_redis_1 bash

TODO
---------------------------------------------

Add Redis support
Include usage instructions
Add unit tests