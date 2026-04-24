# PUT /tasks/recurrences/{recurrence_id}

Update a recurrence template. Manager only.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| recurrence_id | string | The recurrence's unique identifier |

**Auth:** Requires `tasks` whitelist access and manager role on the recurrence.

**Request Body:** All fields optional.
| Field | Type | Description |
|-------|------|-------------|
| title | string | Task title (1-500 chars) |
| description | string | Task description (max 5000 chars) |
| priority | string | `low`, `medium`, `high`, `critical` |
| active_bot_comment | bool | Enable AI bot comments |
| project_id | string | Project UUID |
| ai_instruction_id | string | AI instruction UUID |
| frequency | string | `daily`, `weekly`, or `monthly` |
| day_of_week | integer | 0-6 |
| day_of_month | integer | 1-31 |
| start_date | date | When to start |
| end_date | date | When to stop |
| is_active | bool | Whether recurrence is active |
| members | array | Array of `{username, task_role}` objects |

**Response:** `200 OK`
```json
{
  "status": 200,
  "message": "Recurrence updated successfully",
  "data": { "...recurrence object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access / Only managers can perform this action
- `404` — Recurrence not found
