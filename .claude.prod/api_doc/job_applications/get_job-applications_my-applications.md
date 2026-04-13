# GET /job-applications/my-applications

Get all job applications submitted by the authenticated user. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 20) |

**Response:**
```json
{
  "applications": [
    {
      "id": "uuid",
      "job_post_id": "uuid",
      "job_title": "Software Engineer",
      "status": "submitted",
      "email": "alice@email.com",
      "created_at": "datetime"
    }
  ],
  "total": 3,
  "page": 1,
  "limit": 20
}
```

**Errors:**
- `401` — Not authenticated
