# GET /notifications


List notifications for the authenticated user. Supports pagination, filtering, and optional grouping by entity.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | int | No | 1 | Page number (min: 1) |
| limit | int | No | 20 | Items per page (1-100) |
| is_read | bool | No | null | Filter by read status |
| entity_type | string | No | null | Filter by entity type |
| notification_type | string | No | null | Filter by notification type |
| group_by_entity | bool | No | false | Group notifications by entity |

**Response (flat list, `group_by_entity=false`):**
```json
{
  "notifications": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "notification_type": "comment",
      "entity_type": "task",
      "entity_id": "660e8400-e29b-41d4-a716-446655440000",
      "title": "New comment on Task #123",
      "message": "john.doe commented on your task",
      "metadata": {
        "url": "/tasks/660e8400-e29b-41d4-a716-446655440000",
        "entity_title": "Design Homepage"
      },
      "url": "/tasks/660e8400-e29b-41d4-a716-446655440000",
      "created_by": "john.doe",
      "created_at": "2026-03-10T08:30:00+00:00",
      "is_read": false,
      "read_at": null,
      "is_dismissed": false
    }
  ],
  "total": 42,
  "page": 1,
  "limit": 20,
  "has_more": true
}
```

**Response (grouped, `group_by_entity=true`):**
```json
{
  "groups": [
    {
      "entity_type": "task",
      "entity_id": "660e8400-e29b-41d4-a716-446655440000",
      "entity_title": "Design Homepage",
      "total_count": 5,
      "unread_count": 2,
      "latest": {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "notification_type": "comment",
        "entity_type": "task",
        "entity_id": "660e8400-e29b-41d4-a716-446655440000",
        "title": "New comment on Task #123",
        "message": "john.doe commented on your task",
        "metadata": {},
        "url": "/tasks/660e8400-e29b-41d4-a716-446655440000",
        "created_by": "john.doe",
        "created_at": "2026-03-10T08:30:00+00:00",
        "is_read": false,
        "read_at": null,
        "is_dismissed": false
      }
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
