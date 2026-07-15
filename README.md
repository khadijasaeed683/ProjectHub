# ProjectHub

ProjectHub is a Django-based web application developed to demonstrate advanced Django concepts, including a custom user model, authentication, middleware, rate limiting with Redis, testing, and development best practices.

---

# Features

- Custom User Model (Email Authentication)
- User Registration, Login & Logout
- Custom Django Admin
- Class-Based Views (CBVs)
- Request Logging Middleware
- Redis-based Rate Limiting Middleware
- Role-Based Access Control
- Automated Tests
- Pre-commit Hooks

---

# Technologies Used

- Python 3.13+
- Django 6
- Redis
- Docker
- django-redis / redis-py
- unittest (Django Test Framework)
- pre-commit

---

# Project Structure

```
ProjectHub/
│
├── accounts/
│   ├── models.py
│   ├── managers.py
│   ├── forms.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   └── tests.py
│
├── middleware/
│   └── redis_client.py
│
├── middleware_app/
│   ├── middleware.py
│   └── rate_limit.py
│
├── projects/
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── templates/
│
├── logs/
│   └── request.log
│
├── config/
│
├── requirements.txt
├── .pre-commit-config.yaml
└── README.md
```

---

# Custom User Model

The default Django User model has been replaced with a custom user model.

### Changes

- Email is the unique identifier.
- Username has been removed.
- Users can authenticate using email.
- Superusers are created using email.
- Added user roles:
  - Gold
  - Silver
  - Bronze

---

# Authentication

Implemented using Django Class-Based Views.

Available pages:

- Home
- Register
- Login
- Logout
- Dashboard

---

# Logging Middleware

Every incoming request is logged automatically.

The middleware records:

- Client IP Address
- Request Method
- Requested URL
- Timestamp

Logs are stored inside:

```
logs/request.log
```

Example log:

```
2026-07-14 12:10:21 | 127.0.0.1 | GET | /dashboard/
```

The log file is never overwritten; new logs are appended automatically.

---

# Rate Limiting Middleware

Redis is used to track requests made by each user/IP.

Each key expires automatically after **60 seconds**, creating a rolling one-minute request window.

### Rate Limits

| User Type | Requests / Minute |
|------------|------------------:|
| Gold | 10 |
| Silver | 5 |
| Bronze | 2 |
| Anonymous | 1 |

When the request limit is exceeded, the application returns:

```json
{
    "error": "Too many requests",
    "retry_after": 43,
    "limit": 5
}
```

HTTP Status:

```
429 Too Many Requests
```

---

# Redis

Redis is used only for temporary request counting.

Example Redis keys:

```
user:1
user:5
ip:127.0.0.1
```

Each key automatically expires after 60 seconds.

---

# Middleware Flow

```
Incoming Request
        │
        ▼
Logging Middleware
        │
        ▼
Rate Limiting Middleware
        │
        ▼
Authentication Middleware
        │
        ▼
View
        │
        ▼
Response
```

---

# Testing

The project includes automated tests covering:

- Home View
- Dashboard View
- Registration
- Login
- Logout
- Logging Middleware
- Rate Limiting Middleware
- Role-Based Access Control

Run all tests using:

```bash
python manage.py test
```

---

# Pre-commit Hooks

This project uses pre-commit hooks to automatically check code quality before every commit.

Install pre-commit:

```bash
pip install pre-commit
```

Install the hooks:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

---

# Running the Project

## 1. Clone the repository

```bash
git clone <repository-url>
```

```bash
cd ProjectHub
```

---

## 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start Redis

Using Docker:

```bash
docker run -d --name redis -p 6379:6379 redis
```

If the container already exists:

```bash
docker start redis
```

Verify Redis is running:

```bash
docker ps
```

---

## 5. Apply migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 6. Create a superuser

```bash
python manage.py createsuperuser
```

Enter:

- Email
- Password

---

## 7. Run the development server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

# Useful Commands

Run server:

```bash
python manage.py runserver
```

Run tests:

```bash
python manage.py test
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Run pre-commit:

```bash
pre-commit run --all-files
```

Start Redis:

```bash
docker start redis
```

Open Redis CLI:

```bash
docker exec -it redis redis-cli
```

---

# Future Improvements

- Redis Cache Integration
- API Authentication (JWT)
- Project CRUD Operations
- Task Management Module
- Team Invitations
- Email Verification
- Celery Background Tasks
- Celery Beat Scheduled Tasks
- REST API with Django REST Framework
