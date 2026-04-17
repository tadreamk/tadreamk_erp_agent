# GET /tasks/employees/picker

Get a list of active employees for the task member picker. Results are sorted by **co-member frequency** — employees who share the most tasks with the requesting user appear first. Employees with the same frequency are sorted alphabetically by username. All authenticated users can access this endpoint.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by username, email, or name (up to 50 results) |

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

The response format is unchanged. The frequency value is used only for sorting and is not included in the response.

**Errors:**
- `401` — Not authenticated
