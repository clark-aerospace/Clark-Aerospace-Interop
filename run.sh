#!/bin/bash

# start virtualenv
source venv/bin/activate

# start AUVSI_System app
cd AUVSI_System
python manage.py runserver
