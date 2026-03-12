# PUT /company-events/{event_id}


Update a company event. Requires `company-events` whitelist access. All fields are optional; only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| event_id | UUID | Company event unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Event title (1-500 chars) |
| description | string | No | Event description |
| location | string | No | Event location (max 500 chars) |
| start_time | datetime | No | Event start date and time (ISO 8601) |
| end_time | datetime | No | Event end date and time (ISO 8601) |
| participants | string[] | No | Updated list of employee usernames |
| reminder_at | datetime | No | Reminder datetime (must be in the future and before start_time) |

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Updated Team Lunch",
    "description": "Monthly team lunch - new venue",
    "location": "Restaurant ABC",
    "start_time": "2026-03-25T12:00:00+00:00",
    "end_time": "2026-03-25T14:00:00+00:00",
    "participants": ["john.doe", "jane.smith", "bob.wilson"],
    "participant_details": [],
    "participant_count": 3,
    "created_by": "admin",
    "created_by_name": "ADMIN User",
    "updated_by": "admin",
    "updated_by_name": "ADMIN User",
    "created_at": "2026-03-10T08:00:00+00:00",
    "updated_at": "2026-03-11T10:00:00+00:00",
    "is_active": true,
    "reminder_at": "2026-03-24T09:00:00+00:00",
    "reminder_sent": false,
    "can_edit": true,
    "can_delete": true
  },
  "message": "Company event updated successfully"
}
```

**Errors:**
- `400` — Invalid participant usernames / End time must be on or after start time / Reminder must be in the future / Reminder must be before start time
- `401` — Not authenticated
- `403` — No access to manage company events
- `404` — Company event not found
