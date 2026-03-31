# GET /admin/employee-contract/{username}/history

List all historical (non-current) contracts for an employee, ordered by start_date ascending. Requires `employee-contracts` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes | Employee username |

**Response:**
```json
{
  "username": "john_doe",
  "history": [
    {
      "id": "uuid",
      "employee_username": "john_doe",
      "contract_type": "full_time",
      "start_date": "2024-01-01",
      "end_date": "2024-12-31",
      "salary": 50000.00,
      "is_current": false,
      "created_at": "datetime"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employee-contracts whitelist access
