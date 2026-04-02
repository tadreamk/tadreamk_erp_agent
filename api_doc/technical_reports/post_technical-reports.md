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
  "employee_name": "string",
  "title": "string",
  "description": "string",
  "status": "submitted",
  "file_urls": [],
  "technical_admin": "string",
  "technical_admin_name": "string",
  "resolved_at": null,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00",
  "is_active": true,
  "can_resolve": false,
  "can_edit": true
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
