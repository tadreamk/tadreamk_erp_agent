# GET /job-applications/admin

Get all job applications with advanced filtering. Requires `job-applications` whitelist. Returns empty list if no access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| job_post_id | string | No | Filter by job post ID |
| status_filter | string | No | Filter by application status |
| date_from | string | No | Filter by start date (YYYY-MM-DD) |
| date_to | string | No | Filter by end date (YYYY-MM-DD) |
| search | string | No | Search by name or email |
| sort_by | string | No | Sort field (default: created_at) |
| sort_order | string | No | Sort order (default: desc) |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 100, max: 500) |

**Response:**
```json
{
  "applications": [ { "...application object..." } ],
  "total": 100,
  "page": 1,
  "limit": 100
}
```

**Errors:**
- `400` — Invalid date format
- `401` — Not authenticated
