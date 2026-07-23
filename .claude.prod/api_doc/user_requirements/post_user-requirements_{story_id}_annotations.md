# POST /user-requirements/{story_id}/annotations

Create Annotation. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| story_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| start_offset | integer | Yes |  |
| end_offset | integer | Yes |  |
| highlighted_text | string | Yes |  |
| comment | string | Yes |  |

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
