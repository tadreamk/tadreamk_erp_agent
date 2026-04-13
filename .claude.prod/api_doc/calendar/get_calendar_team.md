# GET /calendar/team

Get team calendar events (approved leaves) for a given month. Defaults to the current month.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| year | int | No | Year (defaults to current year) |
| month | int | No | Month 1–12 (defaults to current month) |
| department | string | No | Filter by department name |
| leave_type | string | No | Filter by leave type |

**Response:**
```json
{
  "year": 2026,
  "month": 3,
  "start_date": "2026-03-01",
  "end_date": "2026-03-31",
  "events": [
    {
      "id": "leave-uuid-2026-03-15",
      "title": "Alice Wong - Annual Leave",
      "date": "2026-03-15",
      "event_type": "leave",
      "is_full_day": true,
      "period": "full",
      "color": "#3b82f6",
      "employee_username": "alice",
      "employee_name": "Alice Wong",
      "leave_type": "Annual Leave",
      "department": "Engineering"
    }
  ],
  "departments": ["Engineering", "Design"]
}
```

**Errors:**
- `400` — Invalid month value
- `401` — Not authenticated
- `403` — Not an employee
