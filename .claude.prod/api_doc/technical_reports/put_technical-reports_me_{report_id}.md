# PUT /technical-reports/me/{report_id}

Edit My Report. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| report_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No |  |
| description | string | No |  |

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
