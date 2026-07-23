# GET /leave/calendar

List Calendar Events. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| from_date | string | No |  |
| to_date | string | No |  |

**Response:**
```json
{
  "events": [
    {
      "employee_username": "string",
      "employee_preferred_name": "string",
      "leave_type": "string",
      "start_date": "date",
      "start_apm": "string",
      "end_date": "date",
      "end_apm": "string",
      "is_swap_pair": false
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
