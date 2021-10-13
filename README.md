### Django Starter Docker

Django Starter project with Docker dev environment and key Django dependencies. Get started in minutes.

- [Django](https://docs.djangoproject.com/en/3.1/)
- Python 3.7

## Local Setup with Docker

For a quick start, you can use the [docker-compose](docker-compose.yml) file. Take a look at its contents to see what is included.

1. Modify `REPO_ROOT` in [.env](.env) file with path to your repo folder.

1. `docker-compose build` to build the container.

1. `docker-compose start postgres` Start postgres and wait for a minute for postgres db to be up.

1. `docker-compose start webserver`. Start the webserver. Go to [localhost:8000](http://localhost:8000) and login with username `admin` and password `admin123`.

To stop the containers use `docker-compose stop` or `docker-compose stop <service-name>`. You can start all containers by running `docker-compose up -d`. Usually postgres takes a minute and Django server times out by then, so you may need to restart the webserver once the postgres is up.

### Using the Dev Container
For development, you may want to a have bash session in the dev container to control when you start or stop the webserver.

1. Adjust the startup `command` of webserver in [docker-compose.yml](docker-compose.yml) and set it to `bash -c "tail -f /dev/null"`. This will have the container just run in the background rather than starting the webserver upon start.

1. `docker-compose up -d` Restart the webserver.

1. `docker-compose exec webserver bash` Start a bash session in the container. From here you can run any bash command.

1. `python manage.py runserver 0.0.0.0:8000` This will start the webserver.

Alternatively you can start a standalone container for the webserver and use it as a development environment (in that case just stop the webserver in [docker-compose.yml](docker-compose.yml) and make sure postgres is up, you will also need to setup the environment vars).

This will start a container that has all the dependencies and start a bash session it.

`docker run --name rp -v /path/to/repo/server:/server -p 8000:8000 rp bash`

## Setup Details

This section breaks down everything that is handled by [docker-compose.yml](docker-compose.yml).

1. `docker-compose build` Runs the [Dockerfile](Dockerfile) to build the Django container with all the dependencies. Follow the steps in Dockerfile to build you custom environment if you would like.

1. `pip3 install -r requirements.txt` Installs python dependencies. See [Dockerfile](Dockerfile) for details.

1. `docker-compose start webserver` Brings up the webserver container. The file also maps the container to local repo and source code, so that your changes will be reflected in the container immediately.

If you look at the `command` section in [docker-compose.yml](docker-compose.yml), you will see that it runs most of the commands below for the initial setup.

1. `python manage.py makemigrations <app-name>` and `python manage.py migrate`. These commands prepare and apply database migrations, which create the database tables for the models we add to Django. You need to run this every time you add or modify a model that requires changes to a database table.

1. `python manage.py load_testing_data`. Creates the admin user and loads sample data. See [load_testing_data.py](server/app/management/commands/load_testing_data.py).

1. `python manage.py runserver 0.0.0.0:8000` Starts the webserver.

1. `python3 manage.py shell` Starts a python shell with Django apps loaded. Super helpful for development. For more details on this, see [iPython](https://ipython.org/) or [Django shell](https://docs.djangoproject.com/en/3.1/ref/django-admin/#shell) docs.

1. The main Django app is [app](server/app), which has files for views, modules etc. See [views.py](server/app/views.py) for view definitions, [templates](server/app/templates) for html files and templates and [urls.py](server/app/urls.py) for urls. See [Django](https://docs.djangoproject.com/en/3.1/) docs for more details.








