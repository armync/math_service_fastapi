# Math Service API

## Overview

Math Service API is a lightweight service that provides basic mathematical operations through a REST API.
It is designed for easy integration, logging, and secure access using API keys.

---

## Features

* Perform basic math operations via API endpoints
* API key authentication for secure usage
* In-memory caching for improved performance
* Request logging with database storage
* Configurable middleware for request/response handling

---

## Project Structure

```
math_service_api_project/
│── .env                      # Environment variables
│── math_requests.db          # SQLite database for request logs
│── logs/app.log              # Application log file
│── math_service/
│   ├── main.py                # Application entry point
│   ├── requirements.txt       # Python dependencies
│   ├── api/routes.py          # API route definitions
│   ├── auth/api_key.py        # API key authentication
│   ├── cache/in_memory.py     # In-memory caching logic
│   ├── core/config.py         # Configuration settings
│   ├── core/middleware.py     # Middleware implementation
│   ├── models/request_log.py  # Database model for logs
│   ├── schemas/operations.py  # Request/response schemas
│   ├── services/db_logger.py  # Database logging service
│   ├── services/logger.py     # Logging service
│   ├── services/math_ops.py   # Math operations service
```

---

## Requirements

* Python 3.9+
* SQLite (included by default with Python)

Install dependencies with:

```bash
pip install -r math_service/requirements.txt
```

---

## Usage

1. Copy `.env` and configure values (such as API key, database settings, etc.).
2. Run the application:

   ```bash
   python math_service/main.py
   ```
3. Access the API at:

   ```
   http://localhost:8000
   ```

---

## API Endpoints

* `POST /add` – Add two numbers
* `POST /subtract` – Subtract two numbers
* `POST /multiply` – Multiply two numbers
* `POST /divide` – Divide two numbers

Each request must include a valid API key in the headers.

---

## Logging

* Requests are logged to `math_requests.db`
* Application logs are stored in `logs/app.log`