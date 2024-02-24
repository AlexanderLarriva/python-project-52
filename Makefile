start:
	python manage.py runserver

gunicorn:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes