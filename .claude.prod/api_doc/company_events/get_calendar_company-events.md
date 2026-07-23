# GET /calendar/company-events

List Company Events In Window. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| from_date | string | Yes | Window start (inclusive). |
| to_date | string | Yes | Window end (inclusive). |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "title": "string",
      "start_time": "datetime",
      "end_time": "datetime",
      "location": "string",
      "participants": [
        {
          "username": {},
          "preferred_name": {},
          "work_email": {}
        }
      ],
      "participant_count": 0,
      "reminder_at": "datetime",
      "reminder_sent": false,
      "event_type": "company_event"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
