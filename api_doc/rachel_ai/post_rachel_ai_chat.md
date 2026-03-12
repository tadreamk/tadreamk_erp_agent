# POST /rachel-ai/chat


Send a message to Rachel AI and receive a response. The last 5 conversations are automatically included as context for the AI. The conversation (user query + bot response) is saved to the database.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| message | string | Yes | The user's message/question |

```json
{
  "message": "How many employees are in the engineering department?"
}
```

**Response:**
```json
{
  "response": "There are currently 15 employees in the Engineering department.",
  "conversation_id": "uuid"
}
```

| Field | Type | Description |
|-------|------|-------------|
| response | string | AI-generated response text |
| conversation_id | UUID | Unique identifier of the saved conversation |

**Errors:**
- `401` — Not authenticated
- `403` — You do not have access to Rachel AI
- `500` — Failed to process your request (AI processing error)
