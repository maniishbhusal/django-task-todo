# Django Task Todo App

## Overview

Welcome to the Django Task Todo App! This simple todo application allows users to create an account, log in with their email and password, and manage their todo items efficiently.

## Features

- **User Authentication:** Users can create accounts with a unique email and password.
- **Email Verification:** Enhanced account security through email verification.
- **Todo Management:** Add, delete, and update todo items effortlessly.

## Getting Started

Follow these steps to run the Django Task Todo App locally:

### Prerequisites

Make sure you have Python and Django installed. 

### 1. Clone the repository to your local machine.
```bash
git clone https://github.com/maniishbhusal/django-task-todo.git
cd django-task-todo
```

### 2. Create a `.env` file in the project root and include the following:
``` bash
SECRET_KEY='django-insecure-&6!ov#!nog*e3gb8pj21c5^cq4k2vq)s!l&e@8cxm=i@toirp('
EMAIL_HOST_USER='YOUR_EMAIL'
EMAIL_HOST_PASSWORD='YOUR_APP_PASSWORD'
```
Replace `'YOUR_EMAIL'` and `'YOUR_APP_PASSWORD'` with your email and the app password generated for email services.




### 3. Create a virtual environment.
``` bash
python -m venv venv
```

### 4. Activate the virtual environment.
* On Windows:
``` bash
venv\Scripts\activate
```

* On macOS/Linux:
``` bash
source venv/bin/activate
```

### 5. Install the project dependencies.
``` bash
pip install -r requirements.txt
```

### 6. Make migrations and migrate
``` bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Django development server.
```bash
python manage.py runserver
```
Open your web browser and visit http://127.0.0.1:8000/ to access the app.

## Project Demo

https://github.com/maniishbhusal/django-task-todo/assets/84217955/01f97d5d-015b-484e-a6cc-72b5f2c9b78c


