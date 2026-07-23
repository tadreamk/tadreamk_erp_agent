# Expenses API

Base prefixes:
- `/expenses`
- `/expenses/{expense_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /expenses | Authenticated employee | List Expenses | [get_expenses.md](get_expenses.md) |
| POST | /expenses | Authenticated employee | Create Expense Route | [post_expenses.md](post_expenses.md) |
| DELETE | /expenses/{expense_id} | Authenticated employee | Soft Delete Expense Route | [delete_expenses_{expense_id}.md](delete_expenses_{expense_id}.md) |
| GET | /expenses/{expense_id} | Authenticated employee | Get Expense | [get_expenses_{expense_id}.md](get_expenses_{expense_id}.md) |
| PUT | /expenses/{expense_id} | Authenticated employee | Update Expense Route | [put_expenses_{expense_id}.md](put_expenses_{expense_id}.md) |
| PUT | /expenses/{expense_id}/allocation | Authenticated employee | Update Expense Allocation Route | [put_expenses_{expense_id}_allocation.md](put_expenses_{expense_id}_allocation.md) |
| POST | /expenses/{expense_id}/approve | Authenticated employee | Approve Expense Route | [post_expenses_{expense_id}_approve.md](post_expenses_{expense_id}_approve.md) |
| POST | /expenses/{expense_id}/reject | Authenticated employee | Reject Expense Route | [post_expenses_{expense_id}_reject.md](post_expenses_{expense_id}_reject.md) |
| POST | /expenses/{expense_id}/submit | Authenticated employee | Submit Expense Route | [post_expenses_{expense_id}_submit.md](post_expenses_{expense_id}_submit.md) |
