# GET /tasks/timeline/range


Get tasks within a date range for timeline view.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start | date | Yes | Start date of range, inclusive (YYYY-MM-DD) |
| end | date | Yes | End date of range, inclusive (YYYY-MM-DD) |

**Response:**
```json
{
  "tasks": [
    {
      "id": "uuid",
      "slug": "task-abc123",
      "title": "Implement login page",
      "description": "...",
      "priority": "high",
      "status": "in_progress",
      "members": [],
      "active_bot_comment": false,
      "ai_instruction_id": null,
      "start_date": "2025-07-01",
      "end_date": "2025-07-15",
      "project_id": null,
      "project": null,
      "created_at": "2025-06-28T10:00:00+00:00",
      "modified_at": "2025-07-02T14:30:00+00:00",
      "created_by": "john.doe",
      "updated_by": "john.doe"
    }
  ],
  "total": 1,
  "range": {
    "start": "2025-07-01",
    "end": "2025-07-31"
  }
}
```

**Errors:**
- `400` — End date cannot be before start date
- `401` — Not authenticated
