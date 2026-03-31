# GET /tasks/team-overview

Get tasks of the authenticated user's subordinates (direct and indirect) via the employee manager hierarchy.

## Request

**Method:** GET
**Path:** `/api/v1/tasks/team-overview`
**Auth:** Bearer token (any authenticated user)

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `status` | string | No | - | Filter by task status (`not_started`, `in_queue`, `in_progress`, `blocked`, `request_approval`, `completed`, `cancelled`) |
| `priority` | string | No | - | Filter by priority (`low`, `medium`, `high`, `urgent`, `critical`) |
| `project_id` | UUID | No | - | Filter by project ID |
| `page` | int | No | 1 | Page number (min: 1) |
| `limit` | int | No | 50 | Items per page (min: 1, max: 200) |

## Response

### 200 OK

```json
{
  "tasks": [
    {
      "id": "uuid",
      "slug": "fix-login-bug-123456",
      "title": "Fix login bug",
      "description": "...",
      "priority": "high",
      "status": "in_progress",
      "members": [{ "username": "alan", "role": "manager" }],
      "active_bot_comment": false,
      "ai_instruction_id": null,
      "start_date": "2026-03-26",
      "end_date": null,
      "project_id": null,
      "project": null,
      "created_at": "2026-03-26T00:00:00+00:00",
      "modified_at": "2026-03-26T00:00:00+00:00",
      "created_by": "alan",
      "updated_by": "alan"
    }
  ],
  "total": 1,
  "subordinates": ["alan", "alanshareteam", "thanhnguyenhuu"],
  "page": 1,
  "limit": 50
}
```

### 401 Unauthorized

Returned when no valid Bearer token is provided.

```json
{
  "detail": "Not authenticated"
}
```

## Notes

- Uses a recursive CTE on `employees.manager_username` to resolve the full subordinate tree.
- Returns only tasks where a subordinate is a `task_team_member`.
- If the user has no subordinates, returns empty tasks and subordinates lists (not a 403).
- The `subordinates` field lists all resolved subordinate usernames for transparency.
- Tasks are ordered by `modified_at` descending.
