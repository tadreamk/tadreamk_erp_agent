# POST /technical-reports/{report_id}/resolve


Mark a technical report as resolved. Requires `technical-reports` whitelist. Only reports with `submitted` status can be resolved. Sends a notification and email to the employee who filed the report.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| report_id | UUID | Yes | Technical report unique identifier |

**Response:**
```json
{
  "message": "Technical report resolved",
  "status": "resolved"
}
```

**Errors:**
- `400` — Cannot resolve report (current status is not `submitted`)
- `401` — Not authenticated
- `403` — No access to technical reports
- `404` — Technical report not found
