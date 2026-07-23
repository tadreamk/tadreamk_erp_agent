# POST /librarian/confirm-action

Confirm Action. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| proposal_id | string | Yes |  |

**Response:**
```json
{
  "success": false,
  "status_code": 0,
  "response_body": null,
  "deep_link": "string",
  "human_summary": "",
  "conversation_id": "uuid"
}
```

**Errors:**
- `422` — Validation Error
