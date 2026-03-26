# GET /tasks/timeline/range

Get tasks within a date range for timeline view. Only returns tasks where the user is a member. Requires authentication and `task` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start | date | Yes | Start date of range (inclusive), format: YYYY-MM-DD |
| end | date | Yes | End date of range (inclusive), format: YYYY-MM-DD |

**Response:**
```json
{
  "tasks": [],
  "total": 5,
  "range": {
    "start": "2024-01-01",
    "end": "2024-01-31"
  }
}
```

**Errors:**
- `400` — End date cannot be before start date
- `401` — Not authenticated
