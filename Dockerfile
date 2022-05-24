FROM python:buster
WORKDIR "/todo_app"
COPY pyproject.toml /todo_app
COPY ./ /todo_app 
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry install 
CMD poetry run flask run -h 0.0.0.0




