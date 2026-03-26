# POST /reimbursement-workflow/{workflow_id}/confirm

Employee confirms that payment has been received. Only callable by the submitting employee when status is `paid`. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The reimbursement workflow's unique identifier |

**Response:**
```json
{
  "message": "Payment confirmed",
  "status": "confirmed"
}
```

**Errors:**
- `400` — Reimbursement not in `paid` status
- `401` — Not authenticated
- `403` — Only the submitting employee can confirm payment
- `404` — Reimbursement not found
