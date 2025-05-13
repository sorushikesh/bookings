# Bookings API – FastAPI CRUD Project

This is a simple FastAPI-based REST API for managing Bookings.  
The goal of this project is to learn and practice the FastAPI framework, focusing on implementing CRUD operations.

---

## Project Objective

The objective of this project is to:

- Understand FastAPI's structure and features
- Learn how to build APIs with FastAPI
- Implement full CRUD (Create, Read, Update, Delete) functionality
- Practice building Python-based backend services

---

## Features

- Create a booking
- Read one or all bookings
- Update an existing booking
- Delete a booking
- Auto-generated interactive API docs with Swagger UI (`/docs`)

---

## Tech Stack

- Framework: FastAPI
- Language: Python 3.10+
- Server: Uvicorn
- Data Storage: PostgreSQL
- Docs: Swagger UI and ReDoc

---

## Project Structure

```

bookings/             
├── main.py           
├── models.py         
├── routes.py         
├── crud.py           
├── database.py       
├── README.md         

````

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/bookings-fastapi.git
cd bookings-fastapi
````

### 2. Create virtual environment & activate

```bash
python -m venv venv
source venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

> 🌐 Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI

---

## API Endpoints

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| GET    | `/bookings`      | Get all bookings       |
| GET    | `/bookings/{id}` | Get a booking by ID    |
| POST   | `/bookings`      | Create a new booking   |
| PUT    | `/bookings/{id}` | Update an existing one |
| DELETE | `/bookings/{id}` | Delete a booking       |

---

## Learnings

* FastAPI routing and dependency injection
* Request & response validation using Pydantic
* Interactive API documentation
* Organizing code for scalability


---

## Author

**Rushikesh Sonawane (sorushikesh07@gmail.com)**
*Developer exploring modern Python backends with FastAPI*
