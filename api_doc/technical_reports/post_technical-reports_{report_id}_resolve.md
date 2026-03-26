# POST /technical-reports/{report_id}/resolve

Mark a technical report as resolved. Report must be in `submitted` status. Sends a resolution notification to the submitter. Requires `technical-reports` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| report_id | UUID | The technical report's unique identifier |

**Response:**
```json
{
  "message": "Technical report resolved",
  "status": "resolved"
}
```

**Errors:**
- `400` — Report is not in `submitted` status
- `401` — Not authenticated
- `403` — Not on technical-reports whitelist
- `404` — Technical report not found
