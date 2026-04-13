# DELETE /reimbursement-workflow/{workflow_id}

Soft delete a reimbursement workflow. Only the submitting employee can delete, and only when status is `pending_pre_approval` or `submitted`. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Response:**
```json
{
  "message": "Reimbursement deleted"
}
```

**Errors:**
- `400` — Cannot delete reimbursement in current status
- `401` — Not authenticated
- `403` — Only the submitting employee can delete
- `404` — Reimbursement not found
