# GET /admin/calendar/team

Get team calendar with approved leaves (admin view). Requires admin/moderator role and `calendar` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| year | int | No | Year (defaults to current year) |
| month | int | No | Month 1–12 (defaults to current month) |

**Response:**
```json
{
  "start_date": "2026-03-01",
  "end_date": "2026-04-01",
  "events": [
    {
      "id": "leave-uuid-2026-03-10",
      "title": "Bob Lee - Sick Leave",
      "date": "2026-03-10",
      "event_type": "leave",
      "is_full_day": true,
      "period": "full",
      "color": "#3b82f6",
      "talent_email": "bob",
      "talent_name": "Bob Lee",
      "status": "approved"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not admin/moderator or missing calendar whitelist
