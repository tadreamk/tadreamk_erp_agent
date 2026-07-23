# GET /calendar/company-events/list

List Company Events Paginated. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No |  |
| start_date | string | No |  |
| end_date | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

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
      "participant_count": 0,
      "reminder_at": "datetime",
      "reminder_sent": false,
      "created_by": "string",
      "created_by_preferred_name": "string",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
