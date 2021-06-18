FROM python:3.8-slim 

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy --ignore-pipfile

COPY newrelic-telegram-relay.py .
COPY telegram.py .
