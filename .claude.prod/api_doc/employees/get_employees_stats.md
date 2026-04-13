# GET /employees/stats

Get employee statistics. Requires `employees` whitelist.

**Response:**
```json
{
  "total": 100,
  "active": 90,
  "inactive": 10
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
