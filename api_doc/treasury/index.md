# Treasury API

Base prefix: `/treasury`

Authentication: Required. All endpoints require `expense-management` whitelist access.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/treasury/dashboard` | Get treasury dashboard summary |
| GET | `/treasury/forecast` | Get cash flow forecast |
| GET | `/treasury/transactions` | List treasury transactions |
| GET | `/treasury/transactions/count` | Count treasury transactions |
| GET | `/treasury/transactions/{transaction_id}` | Get a single transaction |
| POST | `/treasury/transactions` | Create a manual treasury transaction |
| DELETE | `/treasury/transactions/{transaction_id}` | Soft delete a transaction |
| GET | `/treasury/claims/claimable-expenses` | Get claimable expenses for a funding source |
| GET | `/treasury/claims/count` | Count funder claims |
| GET | `/treasury/claims` | List funder claims |
| GET | `/treasury/claims/{claim_id}` | Get a single funder claim |
| POST | `/treasury/claims` | Create a new funder claim |
| PUT | `/treasury/claims/{claim_id}` | Update a draft or submitted claim |
| POST | `/treasury/claims/{claim_id}/submit` | Submit a draft claim to funder |
| POST | `/treasury/claims/{claim_id}/receive` | Mark a submitted claim as received |
| DELETE | `/treasury/claims/{claim_id}` | Delete a draft claim |

## Endpoint Documentation

- [GET /treasury/dashboard](get_treasury_dashboard.md)
- [GET /treasury/forecast](get_treasury_forecast.md)
- [GET /treasury/transactions](get_treasury_transactions.md)
- [GET /treasury/transactions/count](get_treasury_transactions_count.md)
- [GET /treasury/transactions/{transaction_id}](get_treasury_transactions_{transaction_id}.md)
- [POST /treasury/transactions](post_treasury_transactions.md)
- [DELETE /treasury/transactions/{transaction_id}](delete_treasury_transactions_{transaction_id}.md)
- [GET /treasury/claims/claimable-expenses](get_treasury_claims_claimable-expenses.md)
- [GET /treasury/claims/count](get_treasury_claims_count.md)
- [GET /treasury/claims](get_treasury_claims.md)
- [GET /treasury/claims/{claim_id}](get_treasury_claims_{claim_id}.md)
- [POST /treasury/claims](post_treasury_claims.md)
- [PUT /treasury/claims/{claim_id}](put_treasury_claims_{claim_id}.md)
- [POST /treasury/claims/{claim_id}/submit](post_treasury_claims_{claim_id}_submit.md)
- [POST /treasury/claims/{claim_id}/receive](post_treasury_claims_{claim_id}_receive.md)
- [DELETE /treasury/claims/{claim_id}](delete_treasury_claims_{claim_id}.md)
