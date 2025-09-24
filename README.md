## 📦 Modular FastAPI Starter Backend

This is a **starter backend project** built with **FastAPI** following a clean and modular architecture.
It comes with ready-to-use **Authentication (JWT)**, **User module**, database integration, and `.env`-based configuration — perfect as a foundation for larger projects.


## 🗂️ Project Structure

```
.
├── app
│   ├── api/
│   ├── core/
│   │   ├── config.py         # Environment and settings configuration
│   ├── db/
│   │   └── database.py       # Database connection (PostgreSQL or SQLite)
│   ├── main.py              # FastAPI entry point
│   └── modules/
│       ├── auth/            # Authentication module
│       │   ├── dependencies.py
│       │   ├── routes.py
│       │   ├── schemas.py
│       │   └── services.py
│       └── user/            # User module
│           ├── models.py
│           ├── routes.py
│           ├── schemas.py
│           └── services.py
├── database.db
├── .env
├── .env.example
├── requirements.txt
└── .ropeproject
```


## 🚀 Features

✅ Modular structure — `auth` and `user` separated cleanly
✅ JWT authentication (login, register, protected routes)
✅ Forgot/Reset password flow
✅ CORS configuration via `.env`
✅ PostgreSQL or SQLite support
✅ Ready for `/api/v1` route versioning
✅ Auto-generated Swagger docs (`/docs`)


## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/fastapi-starter-backend.git
cd fastapi-starter-backend
```


### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# OR
.venv\Scripts\activate      # Windows
```


### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```


### 4️⃣ Configure environment variables

Copy the `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

**.env example:**

```env
# App info
APP_TITLE=Modular FastAPI API
APP_DESCRIPTION=Backend API for Auth and User Modules
APP_VERSION=1.0.0

# Auth
SECRET_KEY=your_secret
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256

# Database
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/your_db_name
# DATABASE_URL=sqlite:///database.db

# CORS
FRONTEND_URL=http://localhost:3000
```


## 🔐 Generate a Secret Key

Use Python to generate a secure `SECRET_KEY`:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and paste it into `.env` as `SECRET_KEY`.


## 🗄️ Database Setup

Make sure PostgreSQL is running (or use SQLite).
Then create the database:

```bash
psql -U postgres -c "CREATE DATABASE your_db_name;"
```

Or update `.env` to use SQLite for local development:

```env
DATABASE_URL=sqlite:///./database.db
```


## ▶️ Run the Server

From the project root:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


## 🔑 Authentication Endpoints

| Endpoint                       | Method | Description                     |
| ------------------------------ | ------ | ------------------------------- |
| `/api/v1/auth/register`        | POST   | Register a new user             |
| `/api/v1/auth/login`           | POST   | Login and get JWT token         |
| `/api/v1/auth/forgot-password` | POST   | Generate a password reset token |
| `/api/v1/auth/reset-password`  | POST   | Reset password using token      |

Use the JWT token returned from login as a `Bearer Token` in protected routes like:

```
GET /api/v1/users/me
Authorization: Bearer <your_access_token>
```


## 🧱 Future Improvements

* Add role-based access (Admin, User)
* Add email service integration for password reset
* Add unit tests and CI/CD

- Author : Ngusa

## 📜 License

MIT License © 2025
