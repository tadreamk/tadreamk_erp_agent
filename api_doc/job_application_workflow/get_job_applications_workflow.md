# GET /job-applications-workflow


List workflows for the dashboard with filters and pagination.

**Access:** Whitelist (`job-applications`)

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| status | string | No | — | Filter by workflow status (e.g. `submitted`, `exercise_assigned`) |
| bookmark | bool | No | — | Filter by bookmark flag |
| search | string | No | — | Search by username or candidate name |
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
      "status": "exercise_assigned",
      "bookmark": false,
      "positions_count": 2,
      "updated_at": "2026-01-15T10:30:00+00:00"
    }
  ],
  "total": 42,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Whitelist access required
