# POST /reimbursement-workflow/{workflow_id}/pre-approve

Pre-approve a reimbursement request (manager action). Sets status to `pre_approved` and notifies the employee. Only the employee's direct manager can perform this action.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "employee_username": "string",
  "approval_username": "manager_username",
  "status": "pre_approved",
  "total_value": 500.00,
  "file_urls": [],
  "employee_note": "string",
  "created_at": "2024-01-01T00:00:00",
  "can_pre_approve": false,
  "can_pre_reject": false,
  "can_submit_receipts": false
}
```

**Errors:**
- `400` -- Cannot pre-approve in current status (must be `pending_pre_approval`)
- `401` -- Not authenticated
- `403` -- Only the employee's direct manager can pre-approve
- `404` -- Reimbursement not found
