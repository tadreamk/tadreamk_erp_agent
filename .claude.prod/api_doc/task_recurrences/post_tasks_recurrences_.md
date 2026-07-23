# POST /tasks/recurrences/

Create New Recurrence. Public endpoint (no auth).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes |  |
| description | string | No |  |
| priority | string | No |  |
| active_bot_comment | boolean | No |  |
| project_id | string | No |  |
| ai_instruction_id | string | No |  |
| frequency | string | Yes | daily, weekly, or monthly |
| day_of_week | integer | No |  |
| day_of_month | integer | No |  |
| start_date | string | Yes |  |
| end_date | string | No |  |
| members | array[RecurrenceMemberInput] | No |  |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
