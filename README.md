# my-django-nuxt

## How to use

Create a new repository with this repository as the template.

Then migrate the database.
```bash
docker compose run django python manage.py makemigrations
docker compose run django python manage.py migrate
```

After that create a superuser
```bash
docker compose run django python manage.py createsuperuser
```

If other applications (e.g., markdownx) are added, collect static files
```bash
docker compose run django python manage.py collectstatic
```

Before starting the web server, run the below command.
```bash
docker compose run nuxt npm install
```
