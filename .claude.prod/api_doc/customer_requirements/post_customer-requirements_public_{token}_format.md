# POST /customer-requirements/public/{token}/format

Format Public Requirement. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| token | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes | Raw text to be reformatted as Markdown |

**Response:**
```json
{
  "formatted": "string"
}
```

**Errors:**
- `422` — Validation Error
