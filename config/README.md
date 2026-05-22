# Django Todo API

A simple REST API built with Django and Django REST Framework for managing TODO items.

## Features

- Create TODOs
- View all TODOs
- View a single TODO
- Update TODOs
- Delete TODOs
- Pagination
- Logging
- Unit tests
- Deployed online

---

## Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite
- Gunicorn
- Render

---

## API Endpoints

### Get all todos

GET /api/todos/

### Create todo

POST /api/todos/

Example request body:

```json
{
  "title": "Submit Project",
  "description": "Complete Django TODO API project",
  "is_completed": false
}
```

### Get single todo

GET /api/todos/{id}/

### Update todo

PUT /api/todos/{id}/

### Delete todo

DELETE /api/todos/{id}/

---

## Health Check

GET /health/

---

## Running Locally

Clone the repository:

```bash
git clone <your-github-repo-url>
cd django-todo-api
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

---

## Running Tests

```bash
python manage.py test
```

---

## Deployment

The API is deployed on Render.

Live API URL:

```text
https://django-todo-api-1-4sbv.onrender.com/api/todos/
```
## Author
Lesego Sekgala