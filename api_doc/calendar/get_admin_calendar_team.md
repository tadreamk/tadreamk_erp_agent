# GET /admin/calendar/team


Get team calendar with approved leaves for a given month (admin view). Defaults to the current month if no parameters are provided.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| year | int | No | Current year | Calendar year |
| month | int | No | Current month | Calendar month (1-12) |

**Response:**
```json
{
  "start_date": "2026-03-01",
  "end_date": "2026-04-01",
  "events": [
    {
      "id": "leave-550e8400-2026-03-15",
      "title": "John Doe - annual",
      "date": "2026-03-15",
      "event_type": "leave",
      "is_full_day": true,
      "period": null,
      "color": "#3b82f6",
      "talent_email": "john.doe",
      "talent_name": "John Doe",
      "status": "approved"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Admin or moderator access required / No whitelist access to calendar section
