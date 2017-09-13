#!/usr/bin/env bash
# sets up environment vars for mysql connection
# FILE MUST BE SOURCED
echo "Type fs for file storage or db for database storage followed by [ENTER]:"
read storage_type

export HBNB_MYSQL_USER="hbnb_dev"
export HBNB_MYSQL_PWD="hbnb_dev_pwd"
export HBNB_MYSQL_HOST="localhost"
export HBNB_MYSQL_DB="hbnb_dev_db"
export HBNB_TYPE_STORAGE="$storage_type"
