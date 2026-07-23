# PUT /notifications/{notification_id}/unread

Mark As Unread. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| notification_id | string |  |

**Response:**
```json
{
  "success": false,
  "message": "string",
  "data": {}
}
```

**Errors:**
- `422` — Validation Error
