# GET /tasks/employees/picker


Get employee usernames for the task member picker dropdown. Available to all authenticated users.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by username |

**Response:**
```json
{
  "employees": [
    { "username": "john.doe", "work_email": "john@company.com" },
    { "username": "jane.smith", "work_email": "jane@company.com" }
  ]
}
```

**Errors:**
- `401` — Not authenticated
