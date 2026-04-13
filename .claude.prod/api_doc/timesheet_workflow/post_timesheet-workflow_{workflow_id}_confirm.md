# POST /timesheet-workflow/{workflow_id}/confirm

Confirm payment receipt (employee action). Only the employee (owner) can confirm, and only when status is `paid`.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | uuid | Yes | Timesheet workflow ID |

**Response:**
```json
{
  "message": "Payment confirmed",
  "status": "confirmed"
}
```

**Errors:**
- `400` — Cannot confirm at current status (must be `paid`)
- `401` — Not authenticated
- `403` — Only the employee can confirm payment
- `404` — Timesheet not found
