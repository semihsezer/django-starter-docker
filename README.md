### Django Starter Docker

Django Starter project with Docker dev environment and key Django dependencies. Get started in minutes.

- [Django](https://docs.djangoproject.com/en/3.1/)
- Runtime: Docker & Docker-Compose
- Python 3.7
- DB: Postgres
- Background Tasks: Django Background Tasks
- Frontend: Basic Bootstrap with Django Templates
- Basic backend tests with Pytest

## Template Values to Change
1. Replace all occurrences of 'myapp' with shorthand name for this app
   1. This includes `.env` file, `docker-compose.yml`, `render.yml`

## Backend Virtualenv setup (recommended)

1. Start a virtual environment
   python -m venv .venv

2. Activate the virtual environment
   source .venv/bin/activate

3. Install requirements
   pip install -r server/requirements.txt

4. Start the db and other services
   make start_db

5. Run migrations and create initial user
   make init

6. Start the server. Go to (localhost:8000)[localhost:/8000]
   make start_server

7. Load sample data, run: `make load_sample_data`

You can view the server at (localhost:8000)[localhost:/8000].
You can view Django Admin and db at (localhost:8000/admin)[localhost:8000/admin]. Login with admin/Admin123.

## Frontend

1. In the `frontend` directory:
   npm run build

2. Then:
   npm run start

You can view the server at (localhost:3000)[localhost:/3000].

## Backend Docker Setup

For a quick start, you can use the [docker-compose](docker-compose.yml) file. Take a look at its contents to see what is included.

1. Create `.env` file from `.env.template`.
   1.  Modify `REPO_ROOT` variable in [.env](.env) file with path to your repo folder.

2. `docker-compose build` to build the container.

3. `docker-compose up -d` Start web and postgres. For the first time, wait for a minute for postgres to be up, you may need to restart the web container with `docker-compose restart web`.

4. Go to [localhost:8000](http://localhost:8000) and login with username `admin` and password `admin123`.

To stop the containers use `docker-compose stop` or `docker-compose stop <service-name>`.

### Using the Dev Container
For debugging, you may want to a have bash session in the dev container.

1. `docker-compose exec web bash` will open a bash session in the web container.

2. You can also adjust `command` in [docker-compose.yml](docker-compose.yml) and set it to `bash -c "tail -f /dev/null"`. This will have the container just run in the background rather than starting the webserver upon start.


3. `python manage.py runserver 0.0.0.0:8000` This will start the webserver.

## Setup Details

This section breaks down everything that is handled by [docker-compose.yml](docker-compose.yml).

1. `docker-compose build` Runs the [Dockerfile](Dockerfile) to build the Django container with all the dependencies. Follow the steps in Dockerfile to build you custom environment if you would like.

If you look at the `command` section in [docker-compose.yml](docker-compose.yml), you will see that it runs most of the commands below for the initial setup.

1. `python manage.py makemigrations <app-name>` and `python manage.py migrate`. These commands prepare and apply database migrations, which create the database tables for the models we add to Django. You need to run this every time you add or modify a model that requires changes to a database table.

2. `python manage.py load_sample_data`. Creates the admin user and triggers the load sample data command. You need to implement this yourself if you want to load any data at startup in your dev environment. See [load_sample_data.py](server/app/management/commands/load_sample_data.py).

3. `python manage.py runserver 0.0.0.0:8000` Starts the webserver.

4. `python3 manage.py shell` Starts a python shell with Django apps loaded. Very helpful for development. For more details on this, see [iPython](https://ipython.org/) or [Django shell](https://docs.djangoproject.com/en/3.1/ref/django-admin/#shell) docs.

5. The main Django app is [app](server/app), which has files for views, modules etc. See [views.py](server/app/views.py) for view definitions, [templates](server/app/templates) for html files and templates and [urls.py](server/app/urls.py) for urls. See [Django](https://docs.djangoproject.com/en/3.1/) docs for more details.
