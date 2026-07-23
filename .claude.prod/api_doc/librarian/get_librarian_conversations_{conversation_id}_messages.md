# GET /librarian/conversations/{conversation_id}/messages

List Messages. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| conversation_id | string |  |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | integer | No |  |
| offset | integer | No |  |

**Response:**
```json
{
  "messages": [
    {
      "id": "uuid",
      "user_query": "string",
      "bot_response": "string",
      "created_at": "datetime",
      "proposal": {
        "proposal_id": {},
        "kind": {},
        "matched_endpoint": {},
        "http_method": {},
        "path": {},
        "request_body": {},
        "human_summary": {},
        "draft_title": {},
        "draft_body": {},
        "item_url_template": {},
        "response_id_field": {}
      }
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
