# GET /employees/active

List Active For Picker. Requires `)
    entries = employee_crud.list_active_employees_for_picker(db, q=q)
    return {` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| q | string | No |  |

**Response:**
```json
{
  "entries": [
    {
      "username": "string",
      "preferred_name": "string",
      "work_email": "string"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
