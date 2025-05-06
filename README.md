# FastAPI CRUD with Authentication

This project is a simple FastAPI application that provides CRUD functionality for multiple resources (users, items, heroes, teams) with authentication support.

## 📁 Project Structure

```
app/
├── auth.py          # Auth logic (JWT)
├── crud.py          # CRUD operations
├── db.py            # Database setup
├── main.py          # FastAPI app
├── model.py         # Database models
├── schema.py        # Pydantic schemas
├── routes/          # API routes
└── requirements.txt # Dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- FastAPI
- SQLAlchemy or SQLModel
- Uvicorn
- Pydantic
- Any other dependencies listed in `requirements.txt`

### Installation

```bash
# Clone the repository
git clone https://github.com/mmudassir0/fastapi-crud-authentication.git
cd fastapi-crud-authentication

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn app.main:app --reload
```

## 🧩 Features

- ✅ JWT Authentication
- ✅ CRUD for Heroes, Teams, Items, and Users
- ✅ SQLModel / SQLAlchemy integration
- ✅ Modular code structure
- ✅ FastAPI dependency injection

## 📬 API Routes

| Endpoint          | Method | Description            |
|-------------------|--------|------------------------|
| `/auth/login`     | POST   | User login             |
| `/auth/register`  | POST   | User registration      |
| `/hero/`          | GET    | List all heroes        |
| `/team/`          | GET    | List all teams         |
| `/item/`          | GET    | List all items         |
| `/user/`          | GET    | List all users         |
| ...               | ...    | Add more as needed     |


```
DATABASE_URL=postgres:///./test.db
SECRET_KEY=your_jwt_secret
```

## ✍️ Contribution

Feel free to fork the repo and submit pull requests. Contributions are always welcome.
