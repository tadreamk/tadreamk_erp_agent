# POST /expenses/{expense_id}/finish


Mark an expense as finished. The expense must be fully allocated before it can be finished. Upon finishing:
- If linked to a **payslip workflow** in `ceo_approval` status, advances it to `employee_signature` and sends a notification email.
- If linked to a **reimbursement workflow** in `approved` status, marks it as `paid` and sends a notification email.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | Expense ID |

**Response:** Updated expense object with `status: "finished"`.

**Errors:**
- `400` -- Expense is already finished
- `404` -- Expense not found
