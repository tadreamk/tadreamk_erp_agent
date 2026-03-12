# GET /calendar/team/range


Get team calendar for a custom date range.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start_date | date | Yes | Range start date (YYYY-MM-DD) |
| end_date | date | Yes | Range end date (YYYY-MM-DD) |
| department | string | No | Filter by department |
| leave_type | string | No | Filter by leave type |

**Response:**
```json
{
  "start_date": "2026-03-01",
  "end_date": "2026-03-31",
  "events": [
    {
      "id": "leave-550e8400-2026-03-15",
      "title": "John Doe",
      "date": "2026-03-15",
      "event_type": "leave",
      "leave_type": "annual",
      "is_full_day": true,
      "period": null,
      "color": "#3b82f6",
      "employee_username": "john.doe",
      "employee_name": "John Doe",
      "department": "Engineering"
    }
  ]
}
```

**Errors:**
- `400` — End date must be after start date
- `401` — Not authenticated
- `403` — Employee access required
