# Expense Management API

Track and manage company expenses from multiple sources -- payslips, reimbursement workflows, and manual entries. Supports funding allocation from multiple funding sources per expense, a finish workflow that advances linked payslip/reimbursement workflows, and soft deletion.

**Access control:** Whitelist `expense-management` required for all endpoints.

---

## 45. Expense Management

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/expenses` | List all expenses with optional filters and pagination. | [get_expenses.md](./get_expenses.md) |
| `GET` | `/expenses/count` | Get count of expenses matching optional filters. | [get_expenses_count.md](./get_expenses_count.md) |
| `GET` | `/expenses/{expense_id}` | Get full details of a specific expense, including related payroll/reimbursement  | [get_expenses_by_id.md](./get_expenses_by_id.md) |
| `POST` | `/expenses` | Create a new manual expense. | [post_expenses.md](./post_expenses.md) |
| `PUT` | `/expenses/{expense_id}` | Update an existing expense. Only provided fields are updated. | [put_expenses_by_id.md](./put_expenses_by_id.md) |
| `PUT` | `/expenses/{expense_id}/allocation` | Update the funding allocation for an expense. Specifies which funding sources co | [put_expenses_by_id_allocation.md](./put_expenses_by_id_allocation.md) |
| `POST` | `/expenses/{expense_id}/finish` | Mark an expense as finished. The expense must be fully allocated before it can b | [post_expenses_by_id_finish.md](./post_expenses_by_id_finish.md) |
| `DELETE` | `/expenses/{expense_id}` | Soft delete an expense. | [delete_expenses_by_id.md](./delete_expenses_by_id.md) |
