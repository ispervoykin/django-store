#!/bin/bash

python manage.py migrate

python manage.py loaddata fixtures/goods/categories.json

python manage.py loaddata fixtures/goods/products.json

# python manage.py collectstatic

python manage.py runserver 0:8000