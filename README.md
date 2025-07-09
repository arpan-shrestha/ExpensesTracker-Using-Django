# 💸 Django Expense Tracker API

This project is a **RESTful API** built with **Django** and **Django REST Framework** that allows users to manage personal income and expenses. It includes user registration, JWT-based authentication, CRUD operations for transactions, and automatic tax calculations.

---

## 🚀 Features

- ✅ User registration and login (JWT-based)
- ✅ Expense/income tracking (CRUD)
- ✅ Flat or percentage-based tax calculations
- ✅ Superusers can view all records
- ✅ Regular users can only view their own
- ✅ Paginated responses for expense list
- ✅ Secure endpoints with permission handling

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (`djangorestframework-simplejwt`)
- **Database**: SQLite (development)
- **Python**: 3.8+

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/expense-tracker-api.git
cd expense-tracker-api
```

2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
