# GET /employees/active

Get active employees for a picker dropdown. Requires `employees` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by username or name |
| limit | int | No | Max results (default: 50) |

**Response:**
```json
{
  "employees": [
    {
      "id": "uuid",
      "username": "alice",
      "work_email": "alice@company.com",
      "family_name": "Wong",
      "given_name": "Alice"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
