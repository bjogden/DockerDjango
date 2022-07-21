# Docker-Django Template

## What
Dockerized:
- Django
- PostgreSQL

## Why
Get up to speed quicker with an already Dockerized Django + Postgres app.


### Snippets
In "web" Docker container...
- create admin
    - `python manage.py createsuperuser --email admin@example.com --username admin`

- create new app
    - `cd app/apps/`
    - `python ../../manage.py startapp sample`

Citation: https://docs.docker.com/samples/django/