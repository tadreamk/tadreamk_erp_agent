# POST /customer-requirements/public/{token}/attachments

Upload Public Attachment. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| token | string |  |

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | string | Yes |  |

**Response:**
```json
{
  "id": "uuid",
  "filename": "string",
  "url": "string",
  "content_type": "string",
  "size_bytes": 0,
  "uploaded_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
