# POST /reimbursement/me/upload-receipt

Upload Receipt. Requires authentication.

**Request Body:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | string | Yes |  |

**Response:**
```json
{
  "url": "string",
  "admin_url": "string",
  "filename": "string",
  "size": 0
}
```

**Errors:**
- `422` — Validation Error
