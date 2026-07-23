# GET /customer-requirements/public/{token}/attachments

List Public Attachments. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| token | string |  |

**Response:**
```json
[
  {
    "id": "uuid",
    "filename": "string",
    "url": "string",
    "content_type": "string",
    "size_bytes": 0,
    "uploaded_at": "datetime"
  }
]
```

**Errors:**
- `422` — Validation Error
