# GET /hr-requests/me

List My Requests. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "status": "open",
      "attachments": [
        {}
      ],
      "finished_at": "datetime",
      "created_at": "datetime",
      "created_by": "string",
      "requester": {
        "username": "string",
        "preferred_name": {},
        "work_email": {}
      }
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
