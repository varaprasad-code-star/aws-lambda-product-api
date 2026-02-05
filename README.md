# AWS Lambda Product API (Serverless)

A simple serverless REST API built using AWS Lambda and Python.
This project demonstrates how to build and deploy backend APIs
using AWS Free Tier services.

---

## Features
- Serverless architecture using AWS Lambda
- REST API with GET and POST methods
- JSON-based request and response handling
- Deployed using AWS Lambda Function URL
- Tested using browser and curl

---

## Tech Stack
- AWS Lambda
- Python
- REST APIs
- JSON
- GitHub

---

## API Endpoints

### GET Products
**URL:** `/`

**Method:** GET

**Description:**  
Returns a list of products.

**Example Response:**
```json
[
  { "id": 1, "name": "iPhone", "price": 999.99 },
  { "id": 2, "name": "Laptop", "price": 1299.99 }
]
