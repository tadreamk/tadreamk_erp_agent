# GET /contacts/departments


Get list of unique department names for the directory filter dropdown.

**Response:**
```json
{
  "departments": [
    "Engineering",
    "Finance",
    "Human Resources",
    "Marketing"
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access the contact directory
