# Expense Categories API

Base prefix: `/expense-categories`

All endpoints require `expense-management` whitelist.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /expense-categories | List expense categories | [get_expense-categories.md](get_expense-categories.md) |
| POST | /expense-categories | Create an expense category | [post_expense-categories.md](post_expense-categories.md) |
| PUT | /expense-categories/{category_id} | Update an expense category | [put_expense-categories_{category_id}.md](put_expense-categories_{category_id}.md) |
| PUT | /expense-categories/{category_id}/deactivate | Deactivate a category | [put_expense-categories_{category_id}_deactivate.md](put_expense-categories_{category_id}_deactivate.md) |
| PUT | /expense-categories/{category_id}/reactivate | Reactivate a category | [put_expense-categories_{category_id}_reactivate.md](put_expense-categories_{category_id}_reactivate.md) |
