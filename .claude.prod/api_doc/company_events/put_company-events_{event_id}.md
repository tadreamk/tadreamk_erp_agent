# PUT /company-events/{event_id}

Update an existing company event. Requires `company-events` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| event_id | UUID | The event's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Event title |
| description | string | No | Event description |
| location | string | No | Event location |
| start_time | datetime | No | Event start time |
| end_time | datetime | No | Event end time (must be >= start_time) |
| participants | list[string] | No | Usernames of participants |
| reminder_at | datetime | No | Reminder time (must be before start_time and in the future) |

**Response:**
```json
{
  "success": true,
  "data": { "...event object..." },
  "message": "Company event updated successfully"
}
```

**Errors:**
- `400` — Invalid participant usernames, end_time < start_time, or invalid reminder_at
- `401` — Not authenticated
- `403` — No company-events whitelist access
- `404` — Company event not found
