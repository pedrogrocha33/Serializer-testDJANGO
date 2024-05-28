DJANGO=python manage.py

run:
	$(DJANGO) runserver

make:
	$(DJANGO) makemigrations

migrate:
	$(DJANGO) migrate

test:
	$(DJANGO) test

shell:
	$(DJANGO) shell

fmt: 
	black .
	ruff check .

db.up: 
	docker-compose up -d

db.down:
	docker stop gym-series-python-db
