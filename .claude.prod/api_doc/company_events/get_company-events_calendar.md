# GET /company-events/calendar

Get company events within a date range for calendar display. Accessible by all employees.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start_date | date | Yes | Start of date range (YYYY-MM-DD) |
| end_date | date | Yes | End of date range (YYYY-MM-DD) |

**Response:**
```json
{
  "success": true,
  "data": {
    "events": [
      {
        "id": "uuid",
        "title": "string",
        "start_time": "datetime",
        "end_time": "datetime",
        "location": "string"
      }
    ]
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
