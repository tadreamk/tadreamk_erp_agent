# GET /calendar/departments


Get list of departments that have employees, for use as filter options.

**Response:**
```json
{
  "departments": ["Engineering", "Design", "HR", "Finance"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Employee access required
