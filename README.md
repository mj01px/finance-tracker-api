# Finance Tracker API

A backend project built with **FastAPI** and **SQLAlchemy**, designed to help manage and analyze personal finances — including **incomes**, **expenses**, and **tags**, all connected through a relational database.

This API supports **CRUD operations**, **report generation**, and **balance tracking**, offering a clean and scalable architecture ideal for financial applications.

---

## Table of Contents
1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Example Endpoints](#example-endpoints)
5. [Architecture Notes](#architecture-notes) 
6. [Author](#author)

---
## Overview

**Finance Tracker API** centralizes income and expense data to make budget management simple, consistent, and developer-friendly.

It provides endpoints for:
- Creating, listing, updating, and deleting financial entries
- Tagging expenses dynamically
- Calculating balance in real-time

Built with:
- FastAPI for async performance
- SQLAlchemy ORM for database mapping
- Pydantic for data validation
- PostgreSQL for persistence

---

##  Tech Stack

| Layer | Technology |
|-------|-------------|
| Language | Python 3.12 |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Database | PostgreSQL |
| Environment | Python-dotenv |
| Server | Uvicorn |

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
 │   ├── expense.py          # Pydantic schemas for expenses
 │   ├── income.py           # Pydantic schemas for incomes
 │   └── tag.py              # Pydantic schemas for tags
 ├── main.py                 # FastAPI app entry point
 └── utils.py            # Helper functions (e.g., balance calc)

```
--

## Example Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/incomes` | Create a new income |
| `GET` | `/incomes` | List all incomes |
| `POST` | `/expenses` | Create a new expense |
| `GET` | `/expenses` | List all expenses |
| `GET` | `/balance` | Get total income, expenses, and balance |
| `POST` | `/tags` | Create a tag |
| `GET` | `/tags` | List tags |

## Architecture Notes

The project uses:
- **Dependency Injection** via FastAPI `Depends(get_db)`
- **Declarative ORM** with SQLAlchemy
- **Automatic schema validation** via Pydantic
- **Association table** (`expense_tag`) for N:N relationship

This keeps the code **modular**, **testable**, and **ready for production scaling**.

---

## Author

**Mauro Junior**  
Software Engineering Student • Tech Enthusiast  
