# GET /job-posts

List all published job posts with filtering and pagination. No authentication required.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| department | string | No | Filter by department |
| job_type | string | No | Filter by job type |
| search | string | No | Search in title and description |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 20, max: 100) |

**Response:**
```json
{
  "job_posts": [ { "...job post object..." } ],
  "total": 10,
  "page": 1,
  "limit": 20,
  "total_pages": 1,
  "has_next": false,
  "has_prev": false
}
```
