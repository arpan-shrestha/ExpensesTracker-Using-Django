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
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
7. Create Superuser (optional)
```bash
python manage.py createsuperuser
```
9. Run the Server
```bash
python manage.py runserver
```
##🔐 Authentication (JWT)

This API uses JWT tokens for authentication.

## 🔸 Register
#POST /api/auth/register/
```json
{
  "username": "arpan123",
  "email": "arpan@example.com",
  "password": "yourpassword"
}
```
## 🔸 Login
#POST /api/auth/login/
```json
{
  "username": "arpan123",
  "password": "yourpassword"
}
Response:

{
  "refresh": "<refresh-token>",
  "access": "<access-token>"
}
```
Use this access token for all authenticated requests.

##📊 Expense/Income API

All endpoints below require the Authorization header:
```json
Authorization: Bearer <access-token>
Content-Type: application/json
```

##🔸 List All My Expenses (Paginated)
#GET /api/expenses/

##🔸 Add New Expense
#POST /api/expenses/
```json
{
  "title": "Dinner",
  "description": "Dinner at restaurant",
  "amount": 100.0,
  "transaction_type": "debit",
  "tax": 10.0,
  "tax_type": "flat"
}
```
##🔸 Get Specific Expense
#GET /api/expenses/{id}/

##🔸 Update Expense
#PUT /api/expenses/{id}/
```json
{
  "title": "Dinner with Friends",
  "description": "Updated description",
  "amount": 120.0,
  "transaction_type": "debit",
  "tax": 10.0,
  "tax_type": "percentage"
}
```
##🔸 Delete Expense
#DELETE /api/expenses/{id}/

##🧠 Business Logic

Flat tax → total = amount + tax
Percentage tax → total = amount + (amount * tax / 100)
Example:

Amount	Tax Type	Tax	Total
100	flat	10	110.0
100	percent	10	110.0
100	flat	0	100.0

##✅ Permissions

User Type	Can View Own Records	Can View All Records	Can Create/Update/Delete
Superuser	✅	✅	✅
Regular User	✅	❌	✅ (own only)

##📋 API Response Examples
```json
➤ Single Expense
{
  "id": 1,
  "title": "Groceries",
  "description": "Weekly grocery shopping",
  "amount": 100.0,
  "transaction_type": "debit",
  "tax": 10.0,
  "tax_type": "flat",
  "total": 110.0,
  "created_at": "2025-07-01T10:00:00Z",
  "updated_at": "2025-07-01T10:00:00Z"
}
➤ Paginated List
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Groceries",
      "amount": 100.0,
      "transaction_type": "debit",
      "total": 110.0
    },
    {
      "id": 2,
      "title": "Salary",
      "amount": 5000.0,
      "transaction_type": "credit",
      "total": 5000.0
    }
  ]
}
```
🧪 Testing Tips with Postman
```json
Register → /api/auth/register/
Login → /api/auth/login/ → Copy access token
Set Header:
Authorization: Bearer <access-token>
Test /api/expenses/ endpoints
```
🐛 Common Issues

##Issue	Fix
401 Unauthorized	Missing or invalid JWT in Authorization header
400 Bad Request	Missing required fields in POST body
403 Forbidden	Regular user accessing other user's data
CSRF Token missing (HTML forms)	Use @csrf_exempt in dev or enable CSRF in forms
no such table: auth_user	Run python manage.py migrate

##📁 Project Structure (Important Files)
```json
ExpenseTracker/
├── expense/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── ExpenseTracker/
│   ├── settings.py
│   ├── urls.py
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── expenses.html
│   ├── add_expense.html
├── db.sqlite3
└── manage.py
```

##📚 Dependencies
- Django>=4.0
- djangorestframework
- djangorestframework-simplejwt

##Install with:
```bash
pip install -r requirements.txt
```



