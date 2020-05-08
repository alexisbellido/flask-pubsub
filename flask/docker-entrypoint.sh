#!/bin/bash
set -e

export REDIS_HOST=$REDIS_HOST
export REDIS_PORT=$REDIS_PORT

export FLASK_APP=$FLASK_APP
export FLASK_RUN_HOST=$FLASK_RUN_HOST
export FLASK_RUN_PORT=$FLASK_RUN_PORT

if [ "$1" == "development" ]; then
    echo "Running in development mode..."
    export FLASK_ENV=development
    cd $PROJECT_DIR
	exec flask run
else
	exec "$@"
fi
