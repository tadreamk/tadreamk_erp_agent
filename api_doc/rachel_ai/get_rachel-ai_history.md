# GET /rachel-ai/history

Get the authenticated user's conversation history with Rachel AI. Requires `rachel-ai` whitelist access.

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
      "user_query": "How many days of annual leave does Alice have?",
      "bot_response": "Alice has 10 days of annual leave remaining.",
      "created_at": "2024-01-01T10:00:00"
    }
  ],
  "total": 45
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to Rachel AI
