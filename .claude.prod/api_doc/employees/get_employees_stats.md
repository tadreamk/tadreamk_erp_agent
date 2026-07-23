# GET /employees/stats

Get Stats. Requires `employees` whitelist.

**Response:**
```json
{
  "active": 0,
  "inactive": 0,
  "total": 0
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No `employees` whitelist access
- `404` — Not found
