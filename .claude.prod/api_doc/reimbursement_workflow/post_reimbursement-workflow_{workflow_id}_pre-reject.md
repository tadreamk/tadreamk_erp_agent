# POST /reimbursement-workflow/{workflow_id}/pre-reject

Reject a pre-approval request (manager action). Sets status to `rejected` and notifies the employee. Only the employee's direct manager can perform this action.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| note | string | No | Reason for rejection |

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "employee_username": "string",
  "approval_username": "manager_username",
  "status": "rejected",
  "total_value": 500.00,
  "file_urls": [],
  "employee_note": "string\n\n---\nRejection Reason: note",
  "created_at": "2024-01-01T00:00:00"
}
```

**Errors:**
- `400` -- Cannot reject in current status (must be `pending_pre_approval`)
- `401` -- Not authenticated
- `403` -- Only the employee's direct manager can reject
- `404` -- Reimbursement not found
