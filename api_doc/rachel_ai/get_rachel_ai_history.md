# GET /rachel-ai/history


Get paginated conversation history for the current user, ordered by most recent first.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | int | No | Page number (default: 1) |
| limit | int | No | Conversations per page (default: 20) |

**Response:**
```json
{
  "conversations": [
    {
      "id": "uuid",
      "user_query": "How many employees are in engineering?",
      "bot_response": "There are currently 15 employees in the Engineering department.",
      "created_at": "2026-03-10T14:30:00"
    }
  ],
  "total": 42
}
```

| Field | Type | Description |
|-------|------|-------------|
| conversations | array | List of conversation history items |
| conversations[].id | UUID | Conversation unique identifier |
| conversations[].user_query | string | The user's original message |
| conversations[].bot_response | string | Rachel AI's response |
| conversations[].created_at | datetime | When the conversation occurred |
| total | int | Total number of conversations for pagination |

**Errors:**
- `401` — Not authenticated
- `403` — You do not have access to Rachel AI
