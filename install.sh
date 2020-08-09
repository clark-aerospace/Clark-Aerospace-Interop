#!/bin/bash

# create virtualenv
virtualenv venv
source venv/bin/activate

pip install Django
pip install django-jsonify

deactivate
