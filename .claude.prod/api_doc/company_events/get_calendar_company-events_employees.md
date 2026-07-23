# GET /calendar/company-events/employees

List Employees For Picker. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
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
