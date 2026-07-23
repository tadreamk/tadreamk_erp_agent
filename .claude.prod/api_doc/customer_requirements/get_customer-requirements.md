# GET /customer-requirements

List Requirements. Public endpoint (no auth).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| search | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
[
  {
    "id": "uuid",
    "share_token": "string",
    "title": "string",
    "summary": "string",
    "status": "string",
    "share_mode": "string",
    "created_by": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**Errors:**
- `422` — Validation Error
