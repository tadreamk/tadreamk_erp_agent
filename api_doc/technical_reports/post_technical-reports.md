# POST /technical-reports

Submit a new technical report. Sends a submission notification. Requires employee authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Report title |
| description | string | Yes | Report description |
| file_urls | list[string] | No | URLs of supporting files |

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "employee_username": "string",
  "title": "string",
  "description": "string",
  "status": "submitted",
  "file_urls": [],
  "created_at": "2024-01-01T00:00:00"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
