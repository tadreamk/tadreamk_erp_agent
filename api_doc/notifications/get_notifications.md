# GET /notifications

List notifications for the authenticated user. Supports pagination, filtering, and optional grouping by entity. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No | Page number (default: 1, min: 1) |
| limit | integer | No | Items per page (default: 20, min: 1, max: 100) |
| is_read | boolean | No | Filter by read status |
| entity_type | string | No | Filter by entity type |
| notification_type | string | No | Filter by notification type |
| group_by_entity | boolean | No | Group notifications by entity (default: false) |

**Response (flat list):**
```json
{
  "notifications": [
    {
      "id": "uuid",
      "notification_type": "string",
      "entity_type": "string",
      "entity_id": "uuid",
      "title": "string",
      "message": "string",
      "is_read": false,
      "is_dismissed": false,
      "created_at": "2024-01-01T00:00:00"
    }
  ],
  "total": 50,
  "page": 1,
  "limit": 20,
  "has_more": true
}
```

**Response (grouped, when group_by_entity=true):**
```json
{
  "groups": [
    {
      "entity_type": "string",
      "entity_id": "uuid",
      "entity_title": "string",
      "latest": {},
      "total_count": 1,
      "unread_count": 3
    }
  ],
  "total_groups": 10,
  "page": 1,
  "limit": 20,
  "has_more": false
}
```

**Errors:**
- `401` — Not authenticated
