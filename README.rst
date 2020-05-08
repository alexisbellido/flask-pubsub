Publisher and subscriber with Flask and Redis
==================================================================


Docker notes
---------------------------------------------

 Build Flask Docker image.

.. code-block:: bash

    $ cd flask
    $ docker build -t zinibu/python:3.7.6 .

Launch and SSH into Flask container.

.. code-block:: bash

    $ docker run -it --rm --mount type=bind,source=$PWD,target=/code zinibu/python:3.7.6 bash

Run Flask in development mode.
.. code-block:: bash

    $ docker run --rm --mount type=bind,source=$PWD,target=/code -p 5000:5000 zinibu/python:3.7.6 -- /code/docker-entrypoint.sh development