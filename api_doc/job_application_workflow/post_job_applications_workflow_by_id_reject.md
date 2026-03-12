# POST /job-applications-workflow/{workflow_id}/reject


Reject a candidate. Sends a rejection email to the candidate with CC to `head_of_recruitment`.

**Access:** Whitelist (`job-applications`)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | No | Optional rejection reason |

**Request Example:**
```json
{
  "reason": "Position filled by another candidate."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Candidate rejected",
  "new_status": "rejected",
  "rejection_reason": "Position filled by another candidate.",
  "final_decision_by": "hr_manager",
  "final_decision_at": "2026-01-25T09:00:00+00:00"
}
```

**Side Effects:**
- Sets status to `rejected`
- Sends rejection email to the candidate (if email setting `recruitment` is enabled)
- CCs `head_of_recruitment` on the rejection email

**Errors:**
- `400` — Invalid UUID format / workflow not in a decidable status
- `401` — Not authenticated
- `403` — Whitelist access required
- `404` — Workflow not found
