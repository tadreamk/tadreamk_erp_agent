# GET /librarian/conversations

List Conversations. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "conversations": [
    {
      "id": "uuid",
      "user_query": "string",
      "bot_response": "string",
      "created_at": "datetime"
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
