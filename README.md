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
---

## POST Products

**URL:** `/`  
**Method:** POST  

**Description:**  
Adds a new product to the list.

**Example Request:**
```json
{
  "id": 3,
  "name": "Keyboard",
  "price": 79.99
}
