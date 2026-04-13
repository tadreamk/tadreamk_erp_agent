# PUT /technical-reports/{report_id}

Update the title and description of a submitted technical report. Only the report owner can edit, and only while the report is in `submitted` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| report_id | UUID | The technical report's unique identifier |

**Request Body:**
```json
{
  "title": "Updated report title",
  "description": "Updated detailed description of the issue"
}
```

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| title | string | Yes | min 1, max 500 characters |
| description | string | Yes | min 1 character |

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "string",
  "title": "string",
  "description": "string",
  "status": "submitted",
  "file_urls": [],
  "technical_admin": null,
  "resolved_at": null,
  "created_at": "datetime",
  "updated_at": "datetime",
  "is_active": true,
  "can_resolve": false,
  "can_edit": true
}
```

**Errors:**
- `400` — Validation error (empty title or description)
- `401` — Not authenticated
- `403` — Not an employee
- `404` — Report not found, not owner, or not in `submitted` status
