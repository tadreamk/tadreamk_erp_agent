# POST /job-applications-workflow/{workflow_id}/notes

Add a new internal note to a workflow. Sends notifications to mentioned users. Requires `job-applications` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| content | string | Yes | Note content |
| mentioned_users | list[string] | No | Usernames to notify |

**Response:** Created note object

**Errors:**
- `401` — Not authenticated
- `403` — No job-applications whitelist access
- `404` — Workflow not found
