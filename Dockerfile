FROM python:3.10-slim-buster as base
RUN apt-get update &&\
    apt-get install curl -y  &&\
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
WORKDIR "/app"
COPY . . 
RUN poetry config virtualenvs.create false --local && poetry install
FROM base as production
WORKDIR "/app/todo_app"
CMD poetry run  gunicorn -w 1 -b 0.0.0.0:$PORT app:app
FROM base as development
CMD poetry run flask run --host=0.0.0.0
FROM base as test
CMD poetry run pytest




