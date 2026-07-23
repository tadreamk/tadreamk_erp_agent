# GET /exercise-tags

List Exercise Tags. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | ExerciseTagStatusEnum | No |  |
| search | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "name": "string",
      "status": "string",
      "usage_count": 0,
      "is_active": false,
      "created_at": "datetime",
      "created_by": "string",
      "updated_at": "datetime",
      "updated_by": "string"
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
