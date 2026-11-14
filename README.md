# 🎓 Student Information Management System

A web-based application built with Python, Django, HTML, CSS, and MySQL. After logging in, a user can add, view, update, and delete student records, and upload a profile picture for each student.

The project demonstrates Django authentication, models, model forms, URL routing, templates, static and media files, and MySQL integration through the Django ORM.

---

## ✨ Features

- 🔐 Login and logout using Django authentication
- ➕ Add student records
- 📋 View the student list
- 👤 View student details
- ✏️ Update student information
- 🗑️ Delete student records (with a confirmation page)
- 🖼️ Upload student profile pictures
- ✔️ Server-side form validation (unique email and phone, 10-digit phone number)
- 🚫 Custom 404 handling with `get_object_or_404`
- 🗄️ MySQL database through the Django ORM

---

## 🛠️ Technologies Used

- Python
- Django (MVT architecture)
- MySQL
- HTML5 and CSS3
- Django Forms and Django ORM
- Git and GitHub

---

## 📂 Project Structure

```text
student-information-management-system/
├── app19/              # App: models, views, forms, urls
├── proj19/             # Project settings and main urls
├── static/
│   ├── css/
│   └── css/image/
├── templates/
│   └── registration/   # login.html
├── media/              # Uploaded profile pictures (not tracked by Git)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/shivapriya019-bit/student-information-management-system.git
cd student-information-management-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the MySQL database

```sql
CREATE DATABASE proj19db;
```

Then set your MySQL username and password in `proj19/settings.py` under `DATABASES`.

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a user to log in with

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser and log in.

---

## 📖 Project Workflow

- A user logs in with Django's built-in authentication.
- Student details are entered through a Django model form and validated on the server.
- Records are stored in MySQL using the Django ORM.
- The student list links to each student's details, update, and delete pages.
- Profile pictures are saved in the `media/profile_pictures/` folder and shown on the details page.

---

## 🎯 Future Improvements

- Search students
- Pagination
- Restrict edit and delete to specific user roles
- Bootstrap responsive UI
- Export student data to PDF or Excel

---

## 👩‍💻 Author

**Shivapriya**
Python Full Stack Developer (Fresher)
GitHub: [shivapriya019-bit](https://github.com/shivapriya019-bit)# student-information-management-system
