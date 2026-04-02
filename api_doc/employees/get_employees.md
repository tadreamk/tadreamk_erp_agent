# GET /employees

List all employees with filtering. Requires `employees` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by username or email |
| include_inactive | bool | No | Include inactive employees (default: false) |
| department | string | No | Filter by department |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 50) |

**Response:**
```json
{
  "employees": [
    {
      "id": "uuid",
      "username": "alice",
      "work_email": "alice@company.com",
      "position": "Software Engineer",
      "full_name": "Alice Smith",
      "department": "Engineering",
      "manager_username": "bob",
      "is_active": true,
      "start_date": "date",
      "created_at": "datetime"
    }
  ],
  "total": 50,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
