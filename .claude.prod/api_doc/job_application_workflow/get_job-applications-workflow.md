# GET /job-applications-workflow

List all job application workflows for the dashboard. Requires `job-applications` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status |
| bookmark | bool | No | Filter by bookmark |
| search | string | No | Search by username or name |
| sort_by | string | No | Sort field (default: updated_at) |
| sort_order | string | No | Sort order (asc/desc, default: desc) |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
{
  "workflows": [
    {
      "id": "uuid",
      "username": "alice",
      "candidate_name": "Alice Wong",
      "status": "interview",
      "bookmark": false,
      "positions_count": 2,
      "position_titles": ["Software Engineer", "Backend Developer"],
      "updated_at": "datetime"
    }
  ],
  "total": 25,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access
