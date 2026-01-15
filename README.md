### Employee Management API

A secure and scalable Employee Management REST API built using **FastAPI**, featuring **JWT-based authentication**, full **CRUD operations**, and **automated testing**.

---

### Tech Stack

* Python 3.13
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic v2
* JWT Authentication
* Pytest
* Uvicorn

---

### Features

* User authentication using JWT tokens
* Secure password hashing (bcrypt)
* Employee CRUD operations
* Filtering and pagination support
* Protected routes using OAuth2
* Comprehensive test coverage
* OpenAPI (Swagger) documentation

---

### Project Structure

```
employee-management-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── crud.py
│   └── routers/
│       ├── auth.py
│       └── employees.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_employees.py
│
├── venv/
├── README.md
└── requirements.txt
```

---

### Setup Instructions

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd employee-management-api
```

#### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Running the Application

```bash
uvicorn app.main:app --reload
```

* API: `http://127.0.0.1:8000`
* Swagger Docs: `http://127.0.0.1:8000/docs`

---

### Authentication

* Default admin credentials:

  * **Username:** admin
  * **Password:** admin123

* Obtain JWT token via:

  ```
  POST /api/auth/login
  ```

* Use the token in Swagger:

  ```
  Authorization: Bearer <token>
  ```

---

### API Endpoints

#### Auth

* `POST /api/auth/login`

#### Employees

* `POST /api/employees/`
* `GET /api/employees/`
* `GET /api/employees/{id}`
* `PUT /api/employees/{id}`
* `DELETE /api/employees/{id}`

---

### Running Tests

```bash
python -m pytest -v
```

All tests should pass successfully.

---

### Live link

https://employee-management-api-tcbd.onrender.com/docs

---

### Notes

* SQLite is used for simplicity.
* Passwords are never stored in plaintext.
* The requirements.txt file includes fully pinned dependencies to ensure deterministic and  reproducible environment setup across systems.
* The project follows clean architecture and best practices.
