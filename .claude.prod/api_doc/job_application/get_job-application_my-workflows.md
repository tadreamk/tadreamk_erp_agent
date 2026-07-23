# GET /job-application/my-workflows

My Workflows. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| page | integer | No |  |
| page_size | integer | No |  |

**Response:**
```json
{
  "items": [
    {
      "id": "uuid",
      "username": "string",
      "username_preferred_name": "string",
      "candidate_display_name": "string",
      "family_name": "string",
      "given_name": "string",
      "status": "string",
      "bookmark": false,
      "job_application_count": 0,
      "job_post_titles": [
        "string"
      ],
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
