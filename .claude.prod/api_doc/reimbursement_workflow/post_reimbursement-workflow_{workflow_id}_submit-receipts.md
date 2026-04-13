# POST /reimbursement-workflow/{workflow_id}/submit-receipts

Submit receipts after pre-approval (employee action). Uploads receipts, optionally updates the total amount, and transitions status from `pre_approved` to `submitted`. Notifies the Finance team.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file_urls | list[string] | Yes | URLs of supporting documents (receipts) |
| total_value | number | No | Updated total amount in HKD (if actual differs from estimate) |

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "employee_username": "string",
  "approval_username": null,
  "status": "submitted",
  "total_value": 500.00,
  "file_urls": ["https://..."],
  "employee_note": "string",
  "created_at": "2024-01-01T00:00:00"
}
```

**Errors:**
- `400` -- Cannot submit receipts in current status (must be `pre_approved`)
- `401` -- Not authenticated
- `403` -- Only the owner can submit receipts
- `404` -- Reimbursement not found
