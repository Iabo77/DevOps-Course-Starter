FROM python:buster
COPY ./todo_app/ /opt/todo_app
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN ~/.local/bin/poetry install 


