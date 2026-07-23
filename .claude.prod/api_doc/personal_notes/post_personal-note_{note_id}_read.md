# POST /personal-note/{note_id}/read

Mark Read. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| note_id | string |  |

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
