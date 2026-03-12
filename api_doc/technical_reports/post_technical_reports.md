# POST /technical-reports


Create a new technical report. The authenticated employee is recorded as the reporter. Sends a notification and email to the Head of IT.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Report title (1-500 characters) |
| description | string | Yes | Detailed description of the issue (min 1 character) |
| file_urls | string[] | No | List of URLs to supporting files (default: empty list) |

```json
{
  "title": "VPN connection issue",
  "description": "Cannot connect to VPN from office network since this morning.",
  "file_urls": [
    "https://storage.googleapis.com/bucket/technical-reports/screenshot.png"
  ]
}
```

**Response (201 Created):**
```json
{
  "id": "uuid",
  "employee_username": "john.doe",
  "employee_name": "DOE John",
  "title": "VPN connection issue",
  "description": "Cannot connect to VPN from office network since this morning.",
  "status": "submitted",
  "file_urls": ["https://storage.googleapis.com/bucket/technical-reports/screenshot.png"],
  "technical_admin": null,
  "technical_admin_name": null,
  "resolved_at": null,
  "created_at": "2026-03-10T09:00:00",
  "updated_at": null,
  "is_active": true,
  "can_resolve": false
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can submit technical reports
- `422` — Validation error (title/description empty or title too long)
