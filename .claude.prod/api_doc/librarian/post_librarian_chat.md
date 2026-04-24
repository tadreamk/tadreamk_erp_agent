# POST /librarian/chat

Send a message to the Librarian and get a permission-filtered response. The Librarian builds a user context from ReBAC roles, filters the database catalog by table-level and column-level rules, generates SQL with injected row-level WHERE clauses, masks restricted columns, and synthesizes a natural-language answer. Requires `librarian` whitelist access.

**Method:** POST

**Path:** `/api/v1/librarian/chat`

**Authentication:** JWT + whitelist("librarian")

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| message | string | Yes | The user's natural-language question |

**Response:**
```json
{
  "response": "The Librarian's answer to the query...",
  "conversation_id": "uuid"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No librarian whitelist access
