# POST /job-applications-workflow/{workflow_id}/reject

Reject a candidate. Sends rejection email to the candidate. Requires `job-applications` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | No | Rejection reason |

**Response:**
```json
{
  "success": true,
  "message": "Candidate rejected",
  "new_status": "rejected",
  "rejection_reason": "string",
  "final_decision_by": "alice",
  "final_decision_at": "datetime"
}
```

**Errors:**
- `400` — Workflow not in decidable state
- `401` — Not authenticated
- `403` — No job-applications whitelist access
- `404` — Workflow not found
