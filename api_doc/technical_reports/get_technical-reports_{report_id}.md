# GET /technical-reports/{report_id}

Get technical report details. Accessible by the submitting employee or users with `technical-reports` whitelist access. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| report_id | UUID | The technical report's unique identifier |

**Response:** Technical report object

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to view this report
- `404` — Technical report not found
