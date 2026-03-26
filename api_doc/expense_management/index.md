# Expense Management API

Base prefix: `/expenses`

Most endpoints require `expense-management` whitelist. Some actions (finish, reject, get by ID, list) also accept CEO role.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /expenses | `expense-management` whitelist or CEO | List all expenses | [get_expenses.md](get_expenses.md) |
| GET | /expenses/count | `expense-management` whitelist | Get expense count | [get_expenses_count.md](get_expenses_count.md) |
| GET | /expenses/{expense_id} | `expense-management` whitelist or CEO | Get expense by ID | [get_expenses_{expense_id}.md](get_expenses_{expense_id}.md) |
| POST | /expenses | `expense-management` whitelist | Create an expense | [post_expenses.md](post_expenses.md) |
| PUT | /expenses/{expense_id} | `expense-management` whitelist | Update an expense | [put_expenses_{expense_id}.md](put_expenses_{expense_id}.md) |
| PUT | /expenses/{expense_id}/allocation | `expense-management` whitelist | Update funding allocation | [put_expenses_{expense_id}_allocation.md](put_expenses_{expense_id}_allocation.md) |
| POST | /expenses/{expense_id}/finish | `expense-management` whitelist or CEO | Mark expense finished | [post_expenses_{expense_id}_finish.md](post_expenses_{expense_id}_finish.md) |
| POST | /expenses/{expense_id}/reject | CEO only | Reject a payslip/reimbursement/timesheet expense | [post_expenses_{expense_id}_reject.md](post_expenses_{expense_id}_reject.md) |
| DELETE | /expenses/{expense_id} | `expense-management` whitelist | Delete an expense | [delete_expenses_{expense_id}.md](delete_expenses_{expense_id}.md) |
