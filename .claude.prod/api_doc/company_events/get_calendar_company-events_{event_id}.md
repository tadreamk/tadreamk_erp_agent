# GET /calendar/company-events/{event_id}

Get Company Event. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| event_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "location": "string",
  "start_time": "datetime",
  "end_time": "datetime",
  "participants": [
    {
      "username": "string",
      "preferred_name": "string",
      "work_email": "string"
    }
  ],
  "reminder_at": "datetime",
  "reminder_sent": false,
  "is_active": false,
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_by": "string",
  "updated_by_preferred_name": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "can_edit": false,
  "can_delete": false
}
```

**Errors:**
- `422` — Validation Error
