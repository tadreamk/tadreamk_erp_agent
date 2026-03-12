# GET /job-applications/admin


List all job applications with advanced filtering and sorting. Requires admin/moderator role and whitelist access to the `application` section. Returns empty list with `"message": "No access"` if user lacks whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| job_post_id | string (UUID) | No | null | Filter by job post ID |
| status_filter | string | No | null | Filter by application status (e.g., `submitted`, `exercise_assigned`) |
| date_from | string | No | null | Start date filter (format: `YYYY-MM-DD`) |
| date_to | string | No | null | End date filter (format: `YYYY-MM-DD`) |
| search | string | No | null | Search in full_name and email |
| sort_by | string | No | `created_at` | Sort field: `created_at`, `status`, or `full_name` |
| sort_order | string | No | `desc` | Sort direction: `asc` or `desc` |
| skip | int | No | 0 | Number of records to skip (min: 0) |
| limit | int | No | 100 | Max records to return (min: 1, max: 500) |

**Response (200):**
```json
{
  "applications": [ { "...": "..." } ],
  "total": 42,
  "page": 1,
  "limit": 100,
  "message": null
}
```

Each application object follows the same `JobApplicationResponse` schema shown in Section 7.

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid date_from or date_to format (must be YYYY-MM-DD) |
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
