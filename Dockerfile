FROM python:3.10-slim-buster
WORKDIR "/app"
COPY . . 
RUN apt-get update 
RUN   apt-get install curl -y  &&\
      curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry install 
WORKDIR "/app/todo_app"
CMD poetry run  gunicorn -w 1 -b 0.0.0.0:8000 app:app




