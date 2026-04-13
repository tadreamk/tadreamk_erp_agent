# GET /tasks/{slug}

Get a single task by slug. User must be a member of the task. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The task's unique slug identifier |

**Response:** Task object with members

**Errors:**
- `401` — Not authenticated
- `403` — No access to this task
- `404` — Task not found
