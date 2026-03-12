# GET /job-applications-workflow/my-workflows


List workflows belonging to the authenticated user (talent/candidate view).

**Access:** Authenticated (any user)

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| status | string | No | — | Filter by workflow status |
| sort_by | string | No | `updated_at` | Sort field |
| sort_order | string | No | `desc` | Sort order: `asc` or `desc` |
| skip | int | No | `0` | Offset for pagination (>= 0) |
| limit | int | No | `50` | Number of results (1-100) |

**Response:**
```json
{
  "workflows": [
    {
      "id": "uuid-string",
      "username": "candidate1",
      "candidate_name": "John Doe",
      "status": "interview_confirmed",
      "bookmark": false,
      "positions_count": 1,
      "updated_at": "2026-01-15T10:30:00+00:00"
    }
  ],
  "total": 2,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
