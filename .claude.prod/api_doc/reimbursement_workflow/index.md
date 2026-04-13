# Reimbursement Workflow API

Base prefix: `/reimbursement-workflow`

Authentication: Required. Finance/HR endpoints require `reimbursement-workflow` whitelist access. Employee endpoints require authentication.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/reimbursement-workflow/expense-categories` | Get all expense categories (employee) |
| GET | `/reimbursement-workflow/my-reimbursements` | Get reimbursements for the authenticated user |
| POST | `/reimbursement-workflow` | Submit a new reimbursement (employee) |
| POST | `/reimbursement-workflow/upload-document` | Upload a supporting document to OneDrive |
| GET | `/reimbursement-workflow/{workflow_id}` | Get reimbursement workflow details |
| PUT | `/reimbursement-workflow/{workflow_id}` | Update a reimbursement (employee, submitted status only) |
| DELETE | `/reimbursement-workflow/{workflow_id}` | Delete a reimbursement (employee, submitted status only) |
| POST | `/reimbursement-workflow/{workflow_id}/confirm` | Employee confirms payment received |
| POST | `/reimbursement-workflow/{workflow_id}/pre-approve` | Manager pre-approves a purchase request |
| POST | `/reimbursement-workflow/{workflow_id}/pre-reject` | Manager rejects a purchase request |
| POST | `/reimbursement-workflow/{workflow_id}/submit-receipts` | Employee submits receipts after pre-approval |
| GET | `/reimbursement-workflow` | List all reimbursements (Finance) |
| POST | `/reimbursement-workflow/{workflow_id}/approve` | Approve a reimbursement (Finance) |
| POST | `/reimbursement-workflow/{workflow_id}/reject` | Reject a reimbursement (Finance) |
| PUT | `/reimbursement-workflow/{workflow_id}/expense-category` | Set expense category for linked expense (Finance) |
| PUT | `/reimbursement-workflow/{workflow_id}/allocation` | Update funding allocation (Finance) |
| POST | `/reimbursement-workflow/{workflow_id}/send-to-ceo` | Send reimbursement to CEO for approval (Finance) |

## Endpoint Documentation

- [GET /reimbursement-workflow/expense-categories](get_reimbursement-workflow_expense-categories.md)
- [GET /reimbursement-workflow/my-reimbursements](get_reimbursement-workflow_my-reimbursements.md)
- [POST /reimbursement-workflow](post_reimbursement-workflow.md)
- [POST /reimbursement-workflow/upload-document](post_reimbursement-workflow_upload-document.md)
- [GET /reimbursement-workflow/{workflow_id}](get_reimbursement-workflow_{workflow_id}.md)
- [PUT /reimbursement-workflow/{workflow_id}](put_reimbursement-workflow_{workflow_id}.md)
- [DELETE /reimbursement-workflow/{workflow_id}](delete_reimbursement-workflow_{workflow_id}.md)
- [POST /reimbursement-workflow/{workflow_id}/confirm](post_reimbursement-workflow_{workflow_id}_confirm.md)
- [POST /reimbursement-workflow/{workflow_id}/pre-approve](post_reimbursement-workflow_{workflow_id}_pre-approve.md)
- [POST /reimbursement-workflow/{workflow_id}/pre-reject](post_reimbursement-workflow_{workflow_id}_pre-reject.md)
- [POST /reimbursement-workflow/{workflow_id}/submit-receipts](post_reimbursement-workflow_{workflow_id}_submit-receipts.md)
- [GET /reimbursement-workflow (Finance)](get_reimbursement-workflow_finance.md)
- [POST /reimbursement-workflow/{workflow_id}/approve](post_reimbursement-workflow_{workflow_id}_approve.md)
- [POST /reimbursement-workflow/{workflow_id}/reject](post_reimbursement-workflow_{workflow_id}_reject.md)
- [PUT /reimbursement-workflow/{workflow_id}/expense-category](put_reimbursement-workflow_{workflow_id}_expense-category.md)
- [PUT /reimbursement-workflow/{workflow_id}/allocation](put_reimbursement-workflow_{workflow_id}_allocation.md)
- [POST /reimbursement-workflow/{workflow_id}/send-to-ceo](post_reimbursement-workflow_{workflow_id}_send-to-ceo.md)
