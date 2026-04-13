# POST /expenses/{expense_id}/reject

Reject a payslip, reimbursement, or timesheet-linked expense. CEO role required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | The expense's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | Yes | Rejection reason |

**Response:** Updated expense object

**Errors:**
- `400` — Can only reject payslip, reimbursement, or timesheet-linked expenses
- `401` — Not authenticated
- `403` — Only CEO can reject expenses
- `404` — Expense not found
