# POST /grammar/fix

Fix Grammar. Public endpoint (no auth).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| text | string | Yes |  |
| field | string | No |  |
| original | string | No |  |

**Response:**
```json
{
  "corrected": "string",
  "changed": false
}
```

**Errors:**
- `422` — Validation Error
