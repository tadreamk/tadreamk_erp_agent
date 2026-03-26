# GET /employees/{employee_id}/full

Get full employee details including contract and personal particular data. Requires `employees` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_id | UUID | The employee's unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "username": "alice",
  "work_email": "alice@company.com",
  "manager_username": "bob",
  "is_active": true,
  "contract": { "...contract fields..." },
  "personal_particular": { "...personal particular fields..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
- `404` — Employee not found
