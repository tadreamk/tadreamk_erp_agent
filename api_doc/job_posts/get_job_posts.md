# GET /job-posts


List published job posts. No authentication required.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| department | string | No | Filter by department |
| job_type | JobType | No | Filter by job type |
| search | string | No | Search in title and description |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 20, max: 100) |

**Response:**
```json
{
  "job_posts": [ { "..." : "..." } ],
  "total": 15,
  "page": 1,
  "limit": 20,
  "total_pages": 1,
  "has_next": false,
  "has_prev": false
}
```
