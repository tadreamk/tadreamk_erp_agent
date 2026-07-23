# POST /librarian/chat

Chat. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| message | string | Yes |  |
| conversation_id | string | No |  |
| skip_shortlist | boolean | No |  |

**Response:**
```json
{
  "reply": "string",
  "conversation_id": "uuid",
  "steps_taken": 0,
  "proposal": {
    "proposal_id": "string",
    "kind": "string",
    "matched_endpoint": "string",
    "http_method": "string",
    "path": "string",
    "request_body": {},
    "human_summary": "",
    "draft_title": "string",
    "draft_body": "string",
    "item_url_template": "string",
    "response_id_field": "string"
  }
}
```

**Errors:**
- `422` — Validation Error
