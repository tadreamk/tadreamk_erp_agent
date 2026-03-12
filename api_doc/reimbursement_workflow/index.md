# Reimbursement Workflow API

Manages the employee reimbursement lifecycle: employees submit reimbursement requests with supporting documents, the Head of Finance approves or rejects, and employees confirm payment receipt.

**Workflow statuses:** `submitted` -> `approved` -> `paid` -> `completed`; or `submitted` -> `rejected`

**Whitelist requirements:**
- Finance endpoints require whitelist `reimbursement-workflow`
- Employee endpoints require authentication (no whitelist)

---

## 39. Reimbursement Workflow (Employee)

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/api/v1/reimbursement-workflow/expense-categories` | Get all available expense categories for classifying reimbursements. | [get_api_v1_reimbursement_workflow_expense_categories.md](./get_api_v1_reimbursement_workflow_expense_categories.md) |
| `GET` | `/api/v1/reimbursement-workflow/my-reimbursements` | Get reimbursements belonging to the authenticated employee with optional status  | [get_api_v1_reimbursement_workflow_my_reimbursements.md](./get_api_v1_reimbursement_workflow_my_reimbursements.md) |
| `POST` | `/api/v1/reimbursement-workflow` | Create a new reimbursement request. The employee username and approval username  | [post_api_v1_reimbursement_workflow.md](./post_api_v1_reimbursement_workflow.md) |
| `POST` | `/api/v1/reimbursement-workflow/upload-document` | Upload a supporting document to OneDrive and return the file URL. Use the return | [post_api_v1_reimbursement_workflow_upload_document.md](./post_api_v1_reimbursement_workflow_upload_document.md) |
| `GET` | `/api/v1/reimbursement-workflow/{workflow_id}` | Get reimbursement workflow details. Accessible by the employee (owner), the assi | [get_api_v1_reimbursement_workflow_by_id.md](./get_api_v1_reimbursement_workflow_by_id.md) |
| `PUT` | `/api/v1/reimbursement-workflow/{workflow_id}` | Update a reimbursement request. Only allowed when status is `submitted` and only | [put_api_v1_reimbursement_workflow_by_id.md](./put_api_v1_reimbursement_workflow_by_id.md) |
| `DELETE` | `/api/v1/reimbursement-workflow/{workflow_id}` | Soft delete a reimbursement request. Only allowed when status is `submitted` and | [delete_api_v1_reimbursement_workflow_by_id.md](./delete_api_v1_reimbursement_workflow_by_id.md) |
| `POST` | `/api/v1/reimbursement-workflow/{workflow_id}/confirm` | Employee confirms that reimbursement payment has been received. Only allowed whe | [post_api_v1_reimbursement_workflow_by_id_confirm.md](./post_api_v1_reimbursement_workflow_by_id_confirm.md) |
| `GET` | `/api/v1/reimbursement-workflow` | List all reimbursement workflows with optional filtering and pagination (Finance | [get_api_v1_reimbursement_workflow.md](./get_api_v1_reimbursement_workflow.md) |
| `POST` | `/api/v1/reimbursement-workflow/{workflow_id}/approve` | Head of Finance approves a reimbursement request. Requires specifying an expense | [post_api_v1_reimbursement_workflow_by_id_approve.md](./post_api_v1_reimbursement_workflow_by_id_approve.md) |
| `POST` | `/api/v1/reimbursement-workflow/{workflow_id}/reject` | Head of Finance rejects a reimbursement request. Only allowed when status is `su | [post_api_v1_reimbursement_workflow_by_id_reject.md](./post_api_v1_reimbursement_workflow_by_id_reject.md) |
