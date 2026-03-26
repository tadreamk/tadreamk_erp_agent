# GET /whitelist/my-endpoints

Get the current user's accessible ERP endpoints. No admin access required — any authenticated user can call this endpoint.

**Response:**
```json
{
  "username": "alice",
  "endpoints": ["leave-management", "tasks", "expense-management"]
}
```

**Errors:**
- `401` — Not authenticated
