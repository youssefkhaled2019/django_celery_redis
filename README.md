# Django + Celery + Redis + PostgreSQL Project

مشروع Backend مبني باستخدام Django مع دمج Celery لتنفيذ الـ Background Tasks باستخدام Redis كـ Broker و Result Backend، بالإضافة إلى PostgreSQL كقاعدة بيانات.

---

# Features

- Django 5.2
- PostgreSQL Database
- Redis Cache
- Celery Background Tasks
- Celery Retry Mechanism
- django-celery-beat Scheduler
- Logging System
- Async Task Processing
- Environment Variables باستخدام python-decouple

---

# Project Structure

```bash
Main/
│
├── Main/
│   ├── settings.py
│   ├── celery.py
│   ├── urls.py
│   └── ...
│
├── app/
│   ├── tasks.py
│   ├── views.py
│   ├── models.py
│   └── ...
│
├── manage.py
└── README.md
```

---

# Technologies Used

- Python
- Django
- Celery
- Redis
- PostgreSQL
- django-celery-beat

---

# Installation

## 1. Clone Project

```bash
git clone <repo_url>
cd project_name
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

أو:

```bash
pip install django celery redis django-redis django-celery-beat psycopg2-binary python-decouple
```

---

# Environment Variables

أنشئ ملف `.env`

```env
SECRET_KEY=your_secret_key

DEBUG=True

POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

HOST=localhost
PORT=5432

LOCATION=redis://127.0.0.1:6379/1

CELERY_BROKER_URL=redis://127.0.0.1:6379/0
CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/2
```

---

# Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Run Django Server

```bash
python manage.py runserver
```

---

# Run Celery Worker

```bash
celery -A Main worker -l info
```

---

# Run Celery Beat

```bash
celery -A Main beat -l info
```

---

# Run Worker + Beat Together

```bash
celery -A Main worker -B -l info
```

---

# Celery Tasks

المشروع يحتوي على عدة Tasks داخل:

```bash
app/tasks.py
```

## Example

```python
@shared_task
def send_emails():
    pass
```

---

# Retry Task Example

```python
@shared_task(bind=True, max_retries=3)
def send_emails_v2(self):
```

Features:

- Retry Support
- Error Handling
- Logging

---

# Scheduled Tasks

تم استخدام:

```python
django_celery_beat
```

لإنشاء Tasks مجدولة من لوحة التحكم Admin.

---

# Running Tests

```bash
python manage.py test
```

---

# Run Specific Test

```bash
python manage.py test app.tests
```

---

# Example Test

```python
from django.test import TestCase
from app.tasks import send_emails

class CeleryTaskTest(TestCase):

    def test_send_emails_task(self):

        result = send_emails.apply()

        self.assertEqual(result.status, "SUCCESS")
```

---

# Redis Usage

Redis مستخدم في:

- Django Cache
- Celery Broker
- Celery Result Backend

---

# Logging

المشروع يستخدم:

```python
logger.info()
logger.error()
```

لتسجيل الأحداث والأخطاء.

---

# Future Improvements

- Docker Support
- Django REST Framework API
- Flower Monitoring
- CI/CD Pipeline
- Pytest
- Unit & Integration Testing
- Production Deployment

---

# Author

Developed using Django + Celery stack for scalable backend processing.