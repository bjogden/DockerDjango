# Docker-Django Template

## What
Dockerized:
- Django
- PostgreSQL

## Why
Get up to speed quicker with an already Dockerized Django + Postgres app.

## How
1. `docker-compose up`
2. Navigate to http://localhost:8000


### Snippets
In "web" Docker container...
- create admin
    - `python manage.py createsuperuser --email admin@example.com --username admin`

- create new app
    - `cd app/apps/`
    - `python ../../manage.py startapp sample`

Citation: https://docs.docker.com/samples/django/