# GET /employee/my-company-roles

Get the current user's active company roles. Requires authentication.

**Response:**
```json
{
  "roles": [
    {
      "title": "HR Manager",
      "description": "Manages HR operations"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
