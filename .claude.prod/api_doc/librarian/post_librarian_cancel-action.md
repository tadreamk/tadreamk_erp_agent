# POST /librarian/cancel-action

Cancel Action. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| proposal_id | string | Yes |  |

**Response:**
```json
{
  "cancelled": false,
  "proposal_id": "string",
  "conversation_id": "uuid"
}
```

**Errors:**
- `422` — Validation Error
