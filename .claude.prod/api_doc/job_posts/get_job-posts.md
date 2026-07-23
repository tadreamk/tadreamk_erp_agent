# GET /job-posts

List Job Posts. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | JobPostStatusEnum | No |  |
| department | string | No |  |
| job_type | JobTypeEnum | No |  |
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
      "department": "string",
      "job_type": "string",
      "location": "string",
      "experience_years": 0,
      "application_deadline": "date",
      "content_by_lang": {},
      "status": "string",
      "published_at": "datetime",
      "closed_at": "datetime",
      "is_active": false,
      "created_at": "datetime",
      "created_by": "string",
      "created_by_preferred_name": "string",
      "updated_at": "datetime",
      "updated_by": "string",
      "updated_by_preferred_name": "string"
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
