# POST /customer-requirements/{requirement_id}/rotate-token

Rotate Token. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| requirement_id | string |  |

**Response:**
```json
{
  "share_token": "string"
}
```

**Errors:**
- `422` — Validation Error
