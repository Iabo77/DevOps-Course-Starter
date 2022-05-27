FROM python:3.10-slim-buster
WORKDIR "/app"
COPY . . 
RUN apt-get update
RUN apt-get install curl -y 
RUN  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry install 
#WORKDIR "/app/todo_app"
#CMD poetry run gunicorn --bind 0.0.0.0:5000 app:app




