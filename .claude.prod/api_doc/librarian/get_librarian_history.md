# GET /librarian/history

Get the authenticated user's conversation history with the Librarian. Requires `librarian` whitelist access.

**Method:** GET

**Path:** `/api/v1/librarian/history`

**Authentication:** JWT + whitelist("librarian")

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No | Page number (default: 1) |
| limit | integer | No | Items per page (default: 20) |

**Response:**
```json
{
  "conversations": [
    {
      "id": "uuid",
      "user_query": "What is Alice's salary?",
      "bot_response": "Based on your access level, Alice's current salary is...",
      "created_at": "2026-04-17T10:00:00"
    }
  ],
  "total": 12
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No librarian whitelist access
