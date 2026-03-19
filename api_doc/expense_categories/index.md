# Expense Categories API

Manage expense categories used for classifying expenses and funding allocations. Supports soft deactivation/reactivation instead of hard deletion.

**Access control:** Whitelist `expense-management` required for all endpoints.

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/expense-categories` | List expense categories. Optionally include inactive categories. | [get_expense_categories.md](./get_expense_categories.md) |
| `POST` | `/expense-categories` | Create a new expense category. Title must be unique. | [post_expense_categories.md](./post_expense_categories.md) |
| `PUT` | `/expense-categories/{category_id}` | Update an existing expense category. | [put_expense_categories_by_id.md](./put_expense_categories_by_id.md) |
| `PUT` | `/expense-categories/{category_id}/deactivate` | Deactivate an expense category (soft delete). | [put_expense_categories_by_id_deactivate.md](./put_expense_categories_by_id_deactivate.md) |
| `PUT` | `/expense-categories/{category_id}/reactivate` | Reactivate a previously deactivated expense category. | [put_expense_categories_by_id_reactivate.md](./put_expense_categories_by_id_reactivate.md) |
