

.PHONY: migrate 
migrate:
	python manage.py migrate


.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations


.PHONY: runserver
runserver:
	python manage.py runserver


.PHONY: shell
shell:
	python manage.py shell


.PHONY: test
test:
	python -m pytest


.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: update
update: install migrate ;	
