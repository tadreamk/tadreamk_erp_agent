# GET /task-ai-instructions/{instruction_id}

Get Instruction. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| instruction_id | string |  |

**Response:**
```json
{
  "id": "string",
  "title": "string",
  "brief_description": "string",
  "content": "string",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_by": "string",
  "updated_by_preferred_name": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
