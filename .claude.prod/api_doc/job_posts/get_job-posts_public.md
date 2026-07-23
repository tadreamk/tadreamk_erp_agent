# GET /job-posts/public

List Public Job Posts. Public endpoint (no auth).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| department | string | No |  |
| job_type | JobTypeEnum | No |  |
| search | string | No |  |
| lang | JobPostLanguageEnum | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "title": "string",
      "slogan": "string",
      "department": "string",
      "job_type": "string",
      "location": "string",
      "application_deadline": "date",
      "published_at": "datetime",
      "language": "string"
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
