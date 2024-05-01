.PHONY: install
install:
	poetry install

.PHONY: init
init:
	poetry init
	
.PHONY: requirements
requirements:
	pip install -r requirements.txt

.PHONY: runserver
runserver:
	poetry run python manage.py runserver

.PHONY: shell 
shell: 
	poetry run python manage.py shell 

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: apply-migrations
apply-migrations:
		poetry run python manage.py makemigrations
		poetry run python manage.py migrate
		poetry run python manage.py runserver


