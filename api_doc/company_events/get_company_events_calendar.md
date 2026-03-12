# GET /company-events/calendar


Get company events for calendar display within a date range. All employees can view.

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
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "title": "Company Town Hall",
        "start_time": "2026-03-20T09:00:00+00:00",
        "end_time": "2026-03-20T11:00:00+00:00",
        "participant_count": 25,
        "event_type": "company_event"
      }
    ]
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access this resource
