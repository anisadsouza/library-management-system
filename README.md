# 📚 Library Management System

A full-featured **Library Management System** built using **Django**
that allows users to register, browse book categories, explore authors,
and manage a personalized book collection.

This project demonstrates backend development using Django,
authentication handling, database relationships, and clean frontend
integration using HTML and CSS.

------------------------------------------------------------------------

## 🚀 Project Overview

The Library Management System is a web-based application designed to
simulate a digital library environment. Users can:

-   Create an account
-   Log in securely
-   Browse books by category
-   View author listings
-   Add books to their personal collection
-   Remove books from their saved list

The system uses Django's built-in authentication framework and SQLite
database for persistent storage.

------------------------------------------------------------------------

## ✨ Features

-   🔐 User Registration & Login System
-   📚 Category-Based Book Browsing
-   👩‍💼 Author Listing Page
-   ➕ Add to "My Books" Collection
-   ❌ Remove from Collection
-   💎 Clean Modern UI (Responsive)
-   🗂 Organized Project Structure
-   🔄 Migration-Based Database Management

------------------------------------------------------------------------

## 🛠 Technology Stack

  Layer        Technology
  ------------ ----------------------------
  Backend      Python, Django
  Database     SQLite (default Django DB)
  Frontend     HTML5, CSS3
  Versioning   Git & GitHub

------------------------------------------------------------------------

## 🧠 System Architecture

The project follows Django's MVT (Model-View-Template) architecture:

-   **Models** → Define database structure (Books, CartItem)
-   **Views** → Handle business logic and routing
-   **Templates** → Render dynamic HTML content
-   **URLs** → Map routes to views

Authentication is handled using Django's built-in auth system.

------------------------------------------------------------------------

## 📂 Project Structure

    LMS/
    │
    ├── lms/                 # Django project settings & routing
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   ├── views.py
    │   └── wsgi.py
    │
    ├── model/               # Application logic
    │   ├── models.py
    │   ├── admin.py
    │   ├── apps.py
    │   └── migrations/
    │
    ├── templates/           # HTML templates
    ├── static/              # CSS styling
    ├── manage.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Create a Virtual Environment

``` bash
python -m venv venv
```

### 2️⃣ Activate Virtual Environment

**Windows:**

``` bash
venv\Scripts\activate
```

**Mac/Linux:**

``` bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations

``` bash
python manage.py migrate
```

## 🌐 Running the Project Locally

After starting the Django development server:

```bash
python manage.py runserver

You will see output like:

Starting development server at http://127.0.0.1:8000/

### 🔎 Important Note

-   The port number (e.g., `8000`) may be different if that port is
    already in use.
-   If 8000 is busy, Django may run on:
    -   `http://127.0.0.1:8001/`
    -   `http://127.0.0.1:8002/`
-   Always use the exact URL shown in your terminal.

Open in browser:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🔄 Database Management

The project uses Django migrations for database schema control.

To create new migrations:

``` bash
python manage.py makemigrations
```

To apply them:

``` bash
python manage.py migrate
```

------------------------------------------------------------------------

## 🎯 Future Improvements

-   🔍 Book Search Functionality
-   📷 Book Cover Image Upload
-   📊 Admin Dashboard Enhancements
-   ⭐ Ratings & Reviews
-   🌐 Deployment on Cloud Platform (Render / Railway / AWS)
-   🔐 Role-Based User Permissions

------------------------------------------------------------------------

## 📌 Learning Outcomes

This project demonstrates:

-   Django project structuring
-   User authentication workflows
-   Model relationships using ForeignKey
-   Clean UI design integration
-   Git version control workflow
-   Environment variable management
-   Production-ready repository structuring

------------------------------------------------------------------------

## 👩‍💻 Author

**Anisa D'souza**\

**Sharavi Shinde**\

------------------------------------------------------------------------

## 📜 License

This project is for educational purposes.

------------------------------------------------------------------------

> Built with Django 🚀