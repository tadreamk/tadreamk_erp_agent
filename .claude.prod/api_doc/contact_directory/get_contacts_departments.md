# GET /contacts/departments

Get unique departments for the contact directory filter. Requires employee authentication.

**Response:**
```json
{
  "departments": ["Engineering", "Finance", "HR", "Marketing"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access the contact directory
