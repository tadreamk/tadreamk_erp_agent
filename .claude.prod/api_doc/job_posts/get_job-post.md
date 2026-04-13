# GET /job-post

List all job posts (including drafts and closed) with optional filtering. Requires `job-posts` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status_filter | string | No | Filter by status (draft, published, closed) |
| department | string | No | Filter by department |
| job_type | string | No | Filter by job type |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 50) |

**Response:**
```json
{
  "job_posts": [ { "...job post object..." } ],
  "total": 15,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-posts whitelist access
