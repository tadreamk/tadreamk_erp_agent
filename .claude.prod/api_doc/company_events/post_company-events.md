# POST /company-events

Create a new company event. Sends notifications and emails to participants. Requires `company-events` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Event title |
| description | string | No | Event description |
| location | string | No | Event location |
| start_time | datetime | Yes | Event start time |
| end_time | datetime | Yes | Event end time (must be >= start_time) |
| participants | list[string] | No | Usernames of participants |
| reminder_at | datetime | No | Reminder time (must be before start_time and in the future) |

**Response:**
```json
{
  "success": true,
  "data": { "...event object..." },
  "message": "Company event created successfully"
}
```

**Errors:**
- `400` — Invalid participant usernames, end_time < start_time, or invalid reminder_at
- `401` — Not authenticated
- `403` — No company-events whitelist access
