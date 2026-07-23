# GET /job-posts/public/{job_post_id}

Get Public Job Post. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | string |  |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| lang | JobPostLanguageEnum | No |  |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "department": "string",
  "job_type": "string",
  "location": "string",
  "experience_years": 0,
  "application_deadline": "date",
  "published_at": "datetime",
  "language": "string",
  "content": {
    "title": "",
    "slogan": "",
    "about_us": "",
    "description": "",
    "responsibilities": [
      "string"
    ],
    "requirements": [
      "string"
    ],
    "benefits": [
      "string"
    ],
    "preferred_qualifications": [
      "string"
    ]
  }
}
```

**Errors:**
- `422` — Validation Error
