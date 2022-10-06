# DevOps Apprenticeship: Project Exercise

## System Requirements


The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.


## Setting up Trello
### Trello Board creation
To run the application a Trello board needs to created with two lists "To Do" and "Done"; these should be created by default when a new Trello board is createdm or they can be created manually with these exact names.

The board name is unimportant but it would be a good idea to give it a descriptive name  ie'To Do App board' 

### Trello Environmental variables
Environmental variables need to entered in the .env file for the app to work

KEY= Trello account Key
TOKEN= Trello account Token
These can be established by visiting https://trello.com/app-key and the generate token link on same page.

BOARD_ID= the Trello board ID being used
This can be established by querying the Trello API  :
https://api.trello.com/1/members/me/boards?fields=name,url&key={{apiKey}}&token={{apiToken}}
where apiKey and apiToken are the KEY and TOKEN values from above.


## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
 ```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


## Testing

There are unit tests to check correct data is returned from the viewmodel properties and an integration test to check the index.html data is populated with expected data using mocked json data for both list and card trello API

To run pytests from command line 
poetry run pytest -rA 
This will run and provide output from all tests and their names.

to run individual tests use the poetry run pytest -k "keyword" command where keyword is a term within the test title which you wish to run. 
ie poetry run pytest -k "open"

Pytest tests can also be run from VSCode testing tab in the side bar if configured with correct extensions.


## Automated Deployment

There are files required to support automated Ansible deployment located in repository /deployment directory.
These files will need to be copied to the ec2-user home directory on the ansible controller node and executed from this directory using the following command

ansible-playbook ansible-playbook.yml -i ansible-inventory

Required variables can be established following process detailed in Trello environmental variables section

## Docker configuration
Build dev and production images using dockerfile included in repository by running following command from the repo directory
(ensure that the .env file is created and populated with relevant environmental variables.)

Development:
```bash
docker build --target development --tag todo-app:dev .
```
Production(gunicorn):
```bash
docker build --target production --tag todo-app:prod .
```
Run built images using the following commands:

Development: Bound to localhost port 5000 (localhost:5000 in browser)
```bash
docker run  --name todo-app-dev -d  --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app -p 5000:5000 --env-file .env todo-app:dev
```

Live: Bound to localhost port 8000 (localhost:8000 in browser)```bash
docker run  --name todo-app-prod -d -p 8000:8000 --env-file .env todo-app:prod
```

## Azure WebApp deployment
The application will be pushed via the Github action pipeline to Azure Web App available on
https://todo-app-ib.azurewebsites.net/




