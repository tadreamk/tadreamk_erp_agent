# POST /api/v1/reimbursement-workflow/{workflow_id}/confirm


Employee confirms that reimbursement payment has been received. Only allowed when status is `paid` and only by the employee who created it. Transitions status to `completed`.

**Access control:** Must be the reimbursement's employee (owner).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Reimbursement workflow ID |

**Response:**
```json
{
  "message": "Payment confirmed",
  "status": "completed"
}
```

**Errors:**
- `400` -- Cannot confirm payment. Current status: {status}
- `401` -- Not authenticated
- `403` -- Only the employee can confirm payment
- `404` -- Reimbursement workflow not found

---

## 40. Reimbursement Workflow (Finance)
