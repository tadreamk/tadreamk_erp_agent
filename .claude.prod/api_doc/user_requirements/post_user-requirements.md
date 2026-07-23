# POST /user-requirements

Create Story. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes |  |
| content | string | No |  |

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
