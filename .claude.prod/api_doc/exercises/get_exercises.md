# GET /exercises

List Exercises. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | ExerciseStatusEnum | No |  |
| tag_id | string | No |  |
| search | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "title": "string",
      "content": "string",
      "status": "string",
      "tags": [
        {
          "id": {},
          "name": {},
          "status": {}
        }
      ],
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
