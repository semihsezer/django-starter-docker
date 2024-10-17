build:
	docker-compose build

init:
	docker-compose up -d postgres
	python server/manage.py migrate
	python server/manage.py create_admin_user

start:
	docker-compose up -d postgres
	python server/manage.py runserver 0.0.0.0:8000

start_server:
	python server/manage.py runserver 0.0.0.0:8000

start_db:
	docker-compose up -d postgres

start_frontend:
	cd frontend && npm start

stop:
	docker-compose down

load_sample_data:
	python server/manage.py load_sample_data --delete --source=server/app/management/scripts/sample_data.xlsx

test:
	pytest server/app/tests

test_recreate_db:
	pytest server/app/tests --create-db