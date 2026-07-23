# GET /job-application/admin/kanban

Admin Kanban. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| job_post_id | string | No |  |

**Response:**
```json
{
  "columns": {},
  "column_order": [
    "string"
  ]
}
```

**Errors:**
- `422` — Validation Error
