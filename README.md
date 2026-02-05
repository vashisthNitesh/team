# Solak CMS (Django CMS 5 + Tailwind v4)

Modernized team member experience powered by Django 5.2 LTS and django CMS 5.

## Quick start

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Key routes

- `/team/` team grid page
- `/team/<slug>/` premium detail page with CMS placeholders

## Stack

- Django 5.2.x
- django CMS 5.0.x
- django-filer + easy-thumbnails
- djangocms text/picture/link/file/video plugins
- Tailwind CSS v4 via CDN, dark mode enabled
