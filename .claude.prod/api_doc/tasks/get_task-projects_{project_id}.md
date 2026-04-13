# GET /task-projects/{project_id}

Get a task project by ID. Requires `task` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| project_id | UUID | The task project's unique identifier |

**Response:** Task project object

**Errors:**
- `400` — Invalid project ID format
- `401` — Not authenticated
- `403` — No `task` whitelist access
- `404` — Task project not found
