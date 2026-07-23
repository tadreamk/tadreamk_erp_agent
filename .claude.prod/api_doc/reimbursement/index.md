# Reimbursement API

Base prefixes:
- `/reimbursement/finance`
- `/reimbursement/finance/{request_id}`
- `/reimbursement/me`
- `/reimbursement/me/{request_id}`
- `/reimbursement/team`
- `/reimbursement/team/{request_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /reimbursement/finance/requests | Authenticated employee | List Finance Requests | [get_reimbursement_finance_requests.md](get_reimbursement_finance_requests.md) |
| GET | /reimbursement/finance/{request_id} | Authenticated employee | Get Finance Request | [get_reimbursement_finance_{request_id}.md](get_reimbursement_finance_{request_id}.md) |
| PUT | /reimbursement/finance/{request_id}/allocation | Authenticated employee | Update Allocation Route | [put_reimbursement_finance_{request_id}_allocation.md](put_reimbursement_finance_{request_id}_allocation.md) |
| POST | /reimbursement/finance/{request_id}/approve | Authenticated employee | Finance Approve Route | [post_reimbursement_finance_{request_id}_approve.md](post_reimbursement_finance_{request_id}_approve.md) |
| PUT | /reimbursement/finance/{request_id}/expense-category | Authenticated employee | Assign Category Route | [put_reimbursement_finance_{request_id}_expense-category.md](put_reimbursement_finance_{request_id}_expense-category.md) |
| POST | /reimbursement/finance/{request_id}/reject | Authenticated employee | Finance Reject Route | [post_reimbursement_finance_{request_id}_reject.md](post_reimbursement_finance_{request_id}_reject.md) |
| POST | /reimbursement/finance/{request_id}/send-to-ceo | Authenticated employee | Send To Ceo Route | [post_reimbursement_finance_{request_id}_send-to-ceo.md](post_reimbursement_finance_{request_id}_send-to-ceo.md) |
| GET | /reimbursement/me/requests | Authenticated employee | List My Requests | [get_reimbursement_me_requests.md](get_reimbursement_me_requests.md) |
| POST | /reimbursement/me/requests | Authenticated employee | Create My Request | [post_reimbursement_me_requests.md](post_reimbursement_me_requests.md) |
| POST | /reimbursement/me/upload-receipt | Authenticated employee | Upload Receipt | [post_reimbursement_me_upload-receipt.md](post_reimbursement_me_upload-receipt.md) |
| GET | /reimbursement/me/{request_id} | Authenticated employee | Get My Request | [get_reimbursement_me_{request_id}.md](get_reimbursement_me_{request_id}.md) |
| POST | /reimbursement/me/{request_id}/confirm | Authenticated employee | Confirm My Receipt | [post_reimbursement_me_{request_id}_confirm.md](post_reimbursement_me_{request_id}_confirm.md) |
| POST | /reimbursement/me/{request_id}/submit-receipts | Authenticated employee | Submit Receipts Route | [post_reimbursement_me_{request_id}_submit-receipts.md](post_reimbursement_me_{request_id}_submit-receipts.md) |
| GET | /reimbursement/team/requests | Authenticated employee | List Team Requests | [get_reimbursement_team_requests.md](get_reimbursement_team_requests.md) |
| GET | /reimbursement/team/{request_id} | Authenticated employee | Get Team Request | [get_reimbursement_team_{request_id}.md](get_reimbursement_team_{request_id}.md) |
| POST | /reimbursement/team/{request_id}/pre-approve | Authenticated employee | Pre Approve Route | [post_reimbursement_team_{request_id}_pre-approve.md](post_reimbursement_team_{request_id}_pre-approve.md) |
| POST | /reimbursement/team/{request_id}/pre-reject | Authenticated employee | Pre Reject Route | [post_reimbursement_team_{request_id}_pre-reject.md](post_reimbursement_team_{request_id}_pre-reject.md) |
