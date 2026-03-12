# GET /job-post


List all job posts with optional filtering.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | JobPostStatus | No | Filter: `draft`, `published`, `closed` |
| department | string | No | Filter by department |
| job_type | JobType | No | Filter by job type |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 50) |

**Response:**
```json
{
  "job_posts": [ { "..." : "..." } ],
  "total": 30,
  "page": 1,
  "limit": 50
}
```
