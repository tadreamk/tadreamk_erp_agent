# PATCH /tasks/{slug}

Update a task's description, status, priority, active_bot_comment, or dates. User must be a member of the task. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The task's unique slug identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| description | string | No | Updated description |
| status | string | No | Updated status |
| priority | string | No | Updated priority |
| active_bot_comment | string | No | Updated AI bot comment |
| start_date | date | No | Updated start date |
| end_date | date | No | Updated end date |

**Response:**
```json
{
  "status": 200,
  "message": "Task updated successfully",
  "data": { "...updated task object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to this task
- `404` — Task not found
