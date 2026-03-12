# PUT /notification-settings/{category_key}


Toggle an email notification setting on or off. Locked categories cannot be toggled.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_key | string | Notification category identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| is_enabled | bool | Yes | Whether the category should be enabled |

**Response:**
```json
{
  "message": "Setting 'task_comment' updated",
  "setting": {
    "category_key": "task_comment",
    "description": "Email when someone comments on your task",
    "is_enabled": false,
    "is_locked": false,
    "updated_by": "admin",
    "updated_at": "2026-03-10T14:30:00+00:00"
  }
}
```

**Errors:**
- `400` — Category is locked and cannot be toggled
- `401` — Not authenticated
- `403` — No whitelist access to notification-settings
- `404` — Category not found
