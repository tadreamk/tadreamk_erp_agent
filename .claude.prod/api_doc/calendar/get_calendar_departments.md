# GET /calendar/departments

Get unique department names for use in calendar filter dropdowns.

**Response:**
```json
{
  "departments": ["Engineering", "Design", "Marketing"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
