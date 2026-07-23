# GET /notifications/

List Notifications. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| is_read | boolean | No |  |
| entity_type | string | No |  |
| notification_type | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "string",
      "notification_type": "string",
      "entity_type": "string",
      "entity_id": "string",
      "title": "string",
      "message": "string",
      "extra_data": {},
      "created_by": "string",
      "created_at": "datetime",
      "is_read": false,
      "read_at": "datetime",
      "is_dismissed": false,
      "recipient_id": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
