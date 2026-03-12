# DELETE /api/v1/reimbursement-workflow/{workflow_id}


Soft delete a reimbursement request. Only allowed when status is `submitted` and only by the employee who created it.

**Access control:** Must be the reimbursement's employee (owner).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Reimbursement workflow ID |

**Response:**
```json
{
  "message": "Reimbursement deleted"
}
```

**Errors:**
- `400` -- Cannot edit reimbursement. Current status: {status}
- `401` -- Not authenticated
- `403` -- Only the employee can edit their reimbursement
- `404` -- Reimbursement workflow not found
