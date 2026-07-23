# DELETE /personal-note/{note_id}/share/{recipient_username}

Revoke Share. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| note_id | string |  |
| recipient_username | string |  |

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
