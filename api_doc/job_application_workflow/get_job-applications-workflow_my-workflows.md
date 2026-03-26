# GET /job-applications-workflow/my-workflows

List workflows for the authenticated user (talent/candidate view). Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status |
| sort_by | string | No | Sort field (default: updated_at) |
| sort_order | string | No | Sort order (default: desc) |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
{
  "workflows": [ { "...workflow list item..." } ],
  "total": 3,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
