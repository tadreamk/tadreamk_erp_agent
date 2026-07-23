# POST /bank-statements/{statement_id}/attachments

Upload Bank Statement Attachment. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| statement_id | string |  |

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | string | Yes |  |

**Response:**
```json
{
  "attachment": {
    "file_id": "string",
    "filename": "string",
    "file_url": "string",
    "file_size": 0,
    "content_type": "string",
    "is_active": true
  }
}
```

**Errors:**
- `422` — Validation Error
