# Finance Tracker API

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)

A backend project built with **FastAPI** and **SQLAlchemy**, designed to manage and analyze personal finances — including **incomes**, **expenses**, and **tags**, all connected through a relational database.

The API supports **CRUD operations**, **real-time balance tracking**, and **report generation**, offering a clean and scalable architecture ideal for financial applications.

---

## 📜 Overview

**Finance Tracker API** centralizes income and expense data to make budget management simple and developer‑friendly.

It provides endpoints for:

- Creating, listing, updating, and deleting financial entries  
- Dynamic tagging for expenses  
- Real‑time balance calculation  

Built with:

- FastAPI for high performance  
- SQLAlchemy for ORM mapping  
- Pydantic for request/response validation  
- PostgreSQL for persistence  

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Language** | Python 3.12 |
| **Framework** | FastAPI |
| **ORM** | SQLAlchemy |
| **Validation** | Pydantic |
| **Database** | PostgreSQL |
| **Environment** | Python-dotenv |
| **Server** | Uvicorn |

---

## Project Structure

```
app/
 ├── core/
 │   └── database.py         # DB engine, session and Base setup
 ├── models/
 │   ├── expense.py          # Expense model (with N:N relationship)
 │   ├── income.py           # Income model
 │   └── tag.py              # Tag model
 ├── routes/
 │   ├── expense.py          # Expense endpoints
 │   ├── income.py           # Income endpoints
 │   ├── tag.py              # Tag endpoints
 │   └── balance.py          # Financial summary routes
 ├── schemas/
 │   ├── expense.py          # Pydantic schemas (request/response)
 │   ├── income.py
 │   └── tag.py
 ├── main.py                 # FastAPI app entry point
 └── utils.py                # Helper functions (e.g., balance calc)
```

---

## Example Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/incomes` | Create a new income |
| `GET`  | `/incomes` | List all incomes |
| `POST` | `/expenses` | Create a new expense |
| `GET`  | `/expenses` | List all expenses |
| `GET`  | `/balance` | Get total income, expenses, and balance |
| `POST` | `/tags` | Create a tag |
| `GET`  | `/tags` | List all tags |

---

## Architecture Notes

The project uses:

- **Dependency Injection** via FastAPI `Depends(get_db)`  
- **Declarative ORM** using SQLAlchemy  
- **Automatic data validation** with Pydantic  
- **Many‑to‑many association table** (`expense_tag`)  

This ensures the system remains **modular**, **testable**, and **ready for scaling**.

---

## 👤 Author

**Mauro Junior**  
Software Engineering Student • Tech Enthusiast
