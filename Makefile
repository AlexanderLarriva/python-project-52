start:
	python manage.py runserver

gunicorn:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

lint:
	poetry run flake8 task_manager

static:
	python manage.py collectstatic

shell_plus:
	python manage.py shell_plus

shell:
	python manage.py shell

test:
	python manage.py test -v 3 task_manager/

dump:
	python manage.py dumpdata users.CustomUser --indent 2 > customuser_data.json