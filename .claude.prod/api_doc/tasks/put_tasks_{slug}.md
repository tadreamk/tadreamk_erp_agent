# PUT /tasks/{slug}

Update Existing Task. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No |  |
| description | string | No |  |
| priority | string | No |  |
| status | string | No |  |
| active_bot_comment | boolean | No |  |
| start_date | string | No |  |
| end_date | string | No |  |
| project_id | string | No |  |
| ai_instruction_id | string | No |  |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
