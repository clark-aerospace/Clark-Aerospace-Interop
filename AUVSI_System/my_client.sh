#!/bin/bash

if [ "$1" == "run" ] 
then
    python manage.py runserver localhost:8001
fi