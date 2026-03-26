# GET /company-events/employees

Get active employees for the participant picker. Requires `company-events` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by name or username |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "username": "alice",
      "full_name": "Alice Wong",
      "work_email": "alice@company.com"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No company-events whitelist access
