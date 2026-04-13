# POST /technical-reports/{report_id}/assign

Assign a technical report to an IT engineer. Report must be in `submitted` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| report_id | UUID | The report's unique identifier |

**Auth:** Requires `technical-reports` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| assigned_to | string | Yes | Username of the IT engineer to assign |

**Response:** `200 OK`
```json
{
  "message": "Technical report assigned",
  "status": "in_progress",
  "assigned_to": "it_engineer"
}
```

**Errors:**
- `400` — Cannot assign report. Current status: {status}
- `401` — Not authenticated
- `403` — Not on technical-reports whitelist
- `404` — Technical report not found
