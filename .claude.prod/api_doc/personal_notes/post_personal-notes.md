# POST /personal-notes

Create a new personal note. Requires authentication.

**Request Body:**
```json
{
  "title": "string (required, 1-500 chars)",
  "content": "markdown string (optional)",
  "category": "string (default: 'Work')"
}
```

**Response (201):**
```json
{
  "id": "uuid",
  "employee_username": "string",
  "title": "string",
  "content": "markdown string or null",
  "category": "string",
  "shared_with": [],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access personal notes
- `422` — Validation error (e.g., title too long or empty)
