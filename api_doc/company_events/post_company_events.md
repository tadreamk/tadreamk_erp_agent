# POST /company-events


Create a new company event. Requires `company-events` whitelist access. Sends in-app notifications and email notifications to all participants.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Event title (1-500 chars) |
| description | string | No | Event description |
| location | string | No | Event location (max 500 chars) |
| start_time | datetime | Yes | Event start date and time (ISO 8601) |
| end_time | datetime | Yes | Event end date and time (ISO 8601, must be >= start_time) |
| participants | string[] | No | List of employee usernames (default: empty) |
| reminder_at | datetime | No | Reminder datetime (must be in the future and before start_time) |

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Team Lunch",
    "description": "Monthly team lunch",
    "location": "Restaurant XYZ",
    "start_time": "2026-03-25T12:00:00+00:00",
    "end_time": "2026-03-25T14:00:00+00:00",
    "participants": ["john.doe", "jane.smith"],
    "participant_details": [],
    "participant_count": 2,
    "created_by": "admin",
    "created_by_name": "ADMIN User",
    "updated_by": null,
    "updated_by_name": null,
    "created_at": "2026-03-10T08:00:00+00:00",
    "updated_at": null,
    "is_active": true,
    "reminder_at": "2026-03-24T09:00:00+00:00",
    "reminder_sent": false,
    "can_edit": true,
    "can_delete": true
  },
  "message": "Company event created successfully"
}
```

**Side effects:**
- Sends in-app notifications to all participants
- Sends email notifications to all participants

**Errors:**
- `400` — Invalid participant usernames / End time must be on or after start time / Reminder must be in the future / Reminder must be before start time
- `401` — Not authenticated
- `403` — No access to manage company events
