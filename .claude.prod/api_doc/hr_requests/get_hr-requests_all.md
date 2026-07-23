# GET /hr-requests/all

List All Requests. Requires `)
    rows, total = hr_request_service.list_all_requests(
        db,
        status_filter=status_filter,
        q=q,
        page=page,
        limit=limit,
    )
    return {
        ` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| q | string | No |  |
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
