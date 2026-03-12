# GET /company-events/employees


Get employees for the participant picker dropdown. Requires `company-events` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| search | string | No | null | Search by name or email |
| limit | int | No | 50 | Max results (1-100) |

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "username": "john.doe",
      "name": "DOE John",
      "work_email": "john.doe@company.com",
      "department": "Engineering"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to manage company events
