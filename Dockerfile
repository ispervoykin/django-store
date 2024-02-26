FROM python:3.10-slim

RUN mkdir /django_app

WORKDIR /django_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh