# POST /expenses/{expense_id}/finish

Mark an expense as finished. Requires `expense-management` whitelist or CEO role. Payslip, reimbursement, and timesheet expenses require CEO role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | The expense's unique identifier |

**Response:** Updated expense object with status "finished"

**Errors:**
- `400` — Expense is already finished
- `401` — Not authenticated
- `403` — Only CEO can approve payslip, reimbursement, and timesheet expenses
- `404` — Expense not found
