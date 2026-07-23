# PUT /tasks/recurrences/{recurrence_id}

Update Existing Recurrence. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| recurrence_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No |  |
| description | string | No |  |
| priority | string | No |  |
| active_bot_comment | boolean | No |  |
| project_id | string | No |  |
| ai_instruction_id | string | No |  |
| frequency | string | No |  |
| day_of_week | integer | No |  |
| day_of_month | integer | No |  |
| start_date | string | No |  |
| end_date | string | No |  |
| is_active | boolean | No |  |
| members | array[RecurrenceMemberInput] | No |  |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
