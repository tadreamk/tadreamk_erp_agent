# POST /comments/{entity_type}/{entity_id}

Create Thread Comment. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entity_type | string |  |
| entity_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | No |  |
| mentions | array[string] | No |  |
| attachments | array[FileUrlRef] | No |  |

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
