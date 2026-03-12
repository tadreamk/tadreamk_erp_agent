# GET /technical-reports/{report_id}


Get detailed view of a technical report. The report owner sees it with `employee` role; users with `technical-reports` whitelist see it with `admin` role (which enables action flags like `can_resolve`).

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| report_id | UUID | Yes | Technical report unique identifier |

**Response:**
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
  "can_resolve": true
}
```

**`can_resolve`** is `true` only when the user has admin role and the report status is `submitted`.

**Errors:**
- `401` — Not authenticated
- `403` — No access to this technical report
- `404` — Technical report not found
