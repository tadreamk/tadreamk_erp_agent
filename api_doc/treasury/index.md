# Treasury API

Company treasury management with dashboard analytics, cash flow forecasting, manual transactions (injections/withdrawals), and funder claim tracking. Provides real-time visibility into cash position, burn rate, runway, and pending receivables.

**Access control:** Whitelist `expense-management` required for all endpoints.

---

## Treasury Dashboard & Transactions

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/treasury/dashboard` | Get treasury dashboard summary including balance, burn rate, runway, and pending receivables. | [get_treasury_dashboard.md](./get_treasury_dashboard.md) |
| `GET` | `/treasury/forecast` | Get cash flow forecast for upcoming months. | [get_treasury_forecast.md](./get_treasury_forecast.md) |
| `GET` | `/treasury/transactions` | List treasury transactions with optional filters and pagination. | [get_treasury_transactions.md](./get_treasury_transactions.md) |
| `GET` | `/treasury/transactions/count` | Get count of treasury transactions matching optional filters. | [get_treasury_transactions_count.md](./get_treasury_transactions_count.md) |
| `GET` | `/treasury/transactions/{transaction_id}` | Get a single treasury transaction by ID. | [get_treasury_transactions_by_id.md](./get_treasury_transactions_by_id.md) |
| `POST` | `/treasury/transactions` | Create a manual treasury transaction (injection or withdrawal only). | [post_treasury_transactions.md](./post_treasury_transactions.md) |
| `DELETE` | `/treasury/transactions/{transaction_id}` | Soft delete a treasury transaction. Auto-created transactions cannot be deleted. | [delete_treasury_transactions_by_id.md](./delete_treasury_transactions_by_id.md) |
| `GET` | `/treasury/claims/claimable-expenses` | Get finished expenses claimable for a specific funding source. | [get_treasury_claims_claimable_expenses.md](./get_treasury_claims_claimable_expenses.md) |
| `GET` | `/treasury/claims/count` | Get count of funder claims matching optional filters. | [get_treasury_claims_count.md](./get_treasury_claims_count.md) |
| `GET` | `/treasury/claims` | List funder claims with optional filters and pagination. | [get_treasury_claims.md](./get_treasury_claims.md) |
| `GET` | `/treasury/claims/{claim_id}` | Get a single funder claim by ID. | [get_treasury_claims_by_id.md](./get_treasury_claims_by_id.md) |
| `POST` | `/treasury/claims` | Create a new funder claim in draft status. | [post_treasury_claims.md](./post_treasury_claims.md) |
| `PUT` | `/treasury/claims/{claim_id}` | Update a draft or submitted claim. Received claims cannot be updated. | [put_treasury_claims_by_id.md](./put_treasury_claims_by_id.md) |
| `POST` | `/treasury/claims/{claim_id}/submit` | Submit a draft claim to funder. | [post_treasury_claims_by_id_submit.md](./post_treasury_claims_by_id_submit.md) |
| `POST` | `/treasury/claims/{claim_id}/receive` | Mark a submitted claim as received. Creates a treasury inflow transaction. | [post_treasury_claims_by_id_receive.md](./post_treasury_claims_by_id_receive.md) |
| `DELETE` | `/treasury/claims/{claim_id}` | Delete a draft claim. Only draft claims can be deleted. | [delete_treasury_claims_by_id.md](./delete_treasury_claims_by_id.md) |
