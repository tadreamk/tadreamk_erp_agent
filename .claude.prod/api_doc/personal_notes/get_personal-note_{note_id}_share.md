# GET /personal-note/{note_id}/share

List Shares. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| note_id | string |  |

**Response:**
```json
{
  "shares": [
    {
      "id": "string",
      "note_id": "string",
      "recipient_username": "string",
      "recipient_preferred_name": "string",
      "read_at": "datetime",
      "created_at": "datetime"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
