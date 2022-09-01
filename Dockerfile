FROM python:3.10-slim-buster as base
RUN apt-get update &&\
    apt-get install curl -y  &&\
    curl -sSL https://install.python-poetry.org | python3 - 
ENV PATH="${PATH}:/root/.local/bin"
WORKDIR "/app"
COPY . . 
RUN poetry config virtualenvs.create false --local && poetry install
FROM base as development
CMD poetry run flask run --host=0.0.0.0
FROM base as test
CMD poetry run pytest
# Ensure that 'production' is last stage in dockerfile as CD Guthub action does not allow specifying stage. 
FROM base as production
WORKDIR "/app/todo_app"
CMD poetry run  gunicorn -w 1 -b 0.0.0.0:$PORT app:app 