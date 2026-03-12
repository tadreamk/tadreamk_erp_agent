# Payslip Workflow API

Manages the full payslip lifecycle: HR creates payslips in batch, finance confirms and sends for CEO approval, CEO approves or rejects, and employees sign to complete.

**Workflow statuses:** `pending_payment` -> `finance_confirmed` / `ceo_approval` -> `employee_signature` -> `completed`

**Whitelist requirements:**
- HR/Finance endpoints require whitelist `payslip` or `payslip-ceo`
- CEO approval/reject endpoints require whitelist `payslip-ceo`
- Employee endpoints require authentication (no whitelist)

---

## 36. Payslip Workflow (HR)

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/api/v1/payslip-workflow/employees` | Get active employees with contract data for the batch creation page. | [get_api_v1_payslip_workflow_employees.md](./get_api_v1_payslip_workflow_employees.md) |
| `POST` | `/api/v1/payslip-workflow/batch` | Create payslips for multiple employees at once. Also creates a linked expense re | [post_api_v1_payslip_workflow_batch.md](./post_api_v1_payslip_workflow_batch.md) |
| `GET` | `/api/v1/payslip-workflow` | List all payslip workflows (HR view) with optional filtering and pagination. | [get_api_v1_payslip_workflow.md](./get_api_v1_payslip_workflow.md) |
| `GET` | `/api/v1/payslip-workflow/{workflow_id}` | Get payslip workflow details. Accessible by HR, CEO, and the employee (employee  | [get_api_v1_payslip_workflow_by_id.md](./get_api_v1_payslip_workflow_by_id.md) |
| `PUT` | `/api/v1/payslip-workflow/{workflow_id}` | Update payslip field values. Only allowed during `pending_payment` or `finance_c | [put_api_v1_payslip_workflow_by_id.md](./put_api_v1_payslip_workflow_by_id.md) |
| `DELETE` | `/api/v1/payslip-workflow/{workflow_id}` | Soft delete a payslip workflow. Only allowed during `pending_payment` status. Al | [delete_api_v1_payslip_workflow_by_id.md](./delete_api_v1_payslip_workflow_by_id.md) |
| `GET` | `/api/v1/payslip-workflow/my-payslips` | Get payslips belonging to the authenticated employee. Only returns payslips at ` | [get_api_v1_payslip_workflow_my_payslips.md](./get_api_v1_payslip_workflow_my_payslips.md) |
| `POST` | `/api/v1/payslip-workflow/{workflow_id}/sign` | Employee signs/acknowledges a payslip. Only allowed when status is `employee_sig | [post_api_v1_payslip_workflow_by_id_sign.md](./post_api_v1_payslip_workflow_by_id_sign.md) |
| `POST` | `/api/v1/payslip-workflow/{workflow_id}/confirm` | Finance confirms a payslip and sends it to the CEO for approval. Allowed from `p | [post_api_v1_payslip_workflow_by_id_confirm.md](./post_api_v1_payslip_workflow_by_id_confirm.md) |
| `POST` | `/api/v1/payslip-workflow/{workflow_id}/approve` | CEO approves a payslip, advancing it to employee signature. Also marks the linke | [post_api_v1_payslip_workflow_by_id_approve.md](./post_api_v1_payslip_workflow_by_id_approve.md) |
| `POST` | `/api/v1/payslip-workflow/{workflow_id}/reject` | CEO rejects a payslip, sending it back to finance for revision. A rejection comm | [post_api_v1_payslip_workflow_by_id_reject.md](./post_api_v1_payslip_workflow_by_id_reject.md) |
