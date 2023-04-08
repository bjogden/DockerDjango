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
    1. `python manage.py createsuperuser --email admin@example.com --username admin`
    2. Navigate to http://localhost:8000/api/users/ to view users

- create new app
    - `cd app/apps/`
    - `python ../../manage.py startapp sample`

- run shell with django app loaded
    - `python manage.py shell_plus`

### Pre-commit Setup
1. `cd DockerDjango`
2. `cp git-hooks/pre-commit .git/hooks/`
3. `chmod +x .git/hooks/pre-commit`

...or all as one line:
`cd DockerDjango && cp git-hooks/pre-commit .git/hooks/ && chmod +x .git/hooks/pre-commit`

Citation: https://docs.docker.com/samples/django/
