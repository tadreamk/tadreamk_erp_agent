# POST /onboarding/{workflow_id}/notes

Create Note. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes |  |
| mentioned_users | array[string] | No |  |

**Response:**
```json
{
  "id": "uuid",
  "workflow_id": "uuid",
  "username": "string",
  "content": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
