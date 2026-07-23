# POST /calendar/company-events

Create Company Event. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes |  |
| description | string | No |  |
| location | string | No |  |
| start_time | string | Yes |  |
| end_time | string | Yes |  |
| participants | array[string] | No |  |
| reminder_at | string | No |  |

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
