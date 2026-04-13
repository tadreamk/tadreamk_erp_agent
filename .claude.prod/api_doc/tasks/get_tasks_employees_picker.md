# GET /tasks/employees/picker

Get a list of active employees for the task member picker. All authenticated users can access this endpoint.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by username (up to 50 results) |

**Response:**
```json
{
  "employees": [
    {
      "username": "alice",
      "work_email": "alice@company.com"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
