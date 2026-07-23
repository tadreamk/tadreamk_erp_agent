# POST /technical-reports/me/attachments

Upload Attachment. Requires authentication.

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | string | Yes |  |

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
