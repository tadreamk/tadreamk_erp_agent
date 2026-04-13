# GET /personal-notes

List notes owned by or shared with the current user. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | string | No | Filter by category |
| search | string | No | Search in title and content |
| skip | int | No | Number of records to skip (default: 0) |
| limit | int | No | Max records to return (default: 50) |

**Response:**
```json
{
  "notes": [
    {
      "id": "uuid",
      "employee_username": "string",
      "title": "string",
      "content": "markdown string or null",
      "category": "string",
      "shared_with": ["username1", "username2"],
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 10
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access personal notes
