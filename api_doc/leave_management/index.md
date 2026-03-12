# Leave Management API

Complete leave management system covering employee self-service requests, admin review workflows, leave amendments, and entitlement administration.

**Leave types:** `annual`, `sick`, `no_pay`, `maternal`, `swap_off`, `swap_work`, `remote_work`

**Leave request statuses:** `pending`, `approved`, `rejected`, `cancelled`

**Amendment types:** `cancel`, `change`

---

## 31. Leave (Employee)

Self-service endpoints for employees to manage their own leave requests, balances, and entitlements. All endpoints require authentication via the current user's session.

**Prefix:** `/leave`

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/leave/my-requests` | Get the current user's leave requests with optional filtering and pagination. | [get_leave_my_requests.md](./get_leave_my_requests.md) |
| `GET` | `/leave/my-requests/{request_id}` | Get a specific leave request belonging to the current user. | [get_leave_my_requests_by_id.md](./get_leave_my_requests_by_id.md) |
| `POST` | `/leave/request` | Submit a new leave request with one or more date periods. For `annual` and `sick | [post_leave_request.md](./post_leave_request.md) |
| `PUT` | `/leave/my-requests/{request_id}/cancel` | Cancel a pending leave request. Only requests with `pending` status can be cance | [put_leave_my_requests_by_id_cancel.md](./put_leave_my_requests_by_id_cancel.md) |
| `POST` | `/leave/my-requests/{request_id}/documents` | Upload supporting document URLs for a leave request. | [post_leave_my_requests_by_id_documents.md](./post_leave_my_requests_by_id_documents.md) |
| `GET` | `/leave/my-balance` | Get the current user's leave balances across all leave types. Only types with en | [get_leave_my_balance.md](./get_leave_my_balance.md) |
| `GET` | `/leave/my-balance/{leave_type}` | Get the current user's leave balance for a specific leave type. | [get_leave_my_balance_by_id.md](./get_leave_my_balance_by_id.md) |
| `GET` | `/leave/my-entitlements` | Get the current user's leave entitlements. | [get_leave_my_entitlements.md](./get_leave_my_entitlements.md) |
| `PUT` | `/leave/my-requests/{request_id}/request-amendment` | Submit an amendment request for an approved leave. Only approved leave requests  | [put_leave_my_requests_by_id_request_amendment.md](./put_leave_my_requests_by_id_request_amendment.md) |
| `GET` | `/leave/my-requests/{request_id}/amendments` | Get all amendments for a specific leave request belonging to the current user. | [get_leave_my_requests_by_id_amendments.md](./get_leave_my_requests_by_id_amendments.md) |
| `GET` | `/admin/leave/requests` | Get all leave requests with filtering and pagination. | [get_admin_leave_requests.md](./get_admin_leave_requests.md) |
| `GET` | `/admin/leave/requests/pending` | Get leave requests with `pending` status awaiting approval. | [get_admin_leave_requests_pending.md](./get_admin_leave_requests_pending.md) |
| `GET` | `/admin/leave/stats` | Get leave dashboard statistics: counts of pending requests, employees currently  | [get_admin_leave_stats.md](./get_admin_leave_stats.md) |
| `GET` | `/admin/leave/requests/{request_id}` | Get a specific leave request by ID (admin view, no ownership restriction). | [get_admin_leave_requests_by_id.md](./get_admin_leave_requests_by_id.md) |
| `PUT` | `/admin/leave/requests/{request_id}/approve` | Approve a pending leave request. Sends an approval notification and email to the | [put_admin_leave_requests_by_id_approve.md](./put_admin_leave_requests_by_id_approve.md) |
| `PUT` | `/admin/leave/requests/{request_id}/reject` | Reject a pending leave request. Sends a rejection notification and email to the  | [put_admin_leave_requests_by_id_reject.md](./put_admin_leave_requests_by_id_reject.md) |
| `GET` | `/admin/leave/calendar` | Get employees who are on approved leave for a specific date. | [get_admin_leave_calendar.md](./get_admin_leave_calendar.md) |
| `GET` | `/admin/leave/balance/{employee_username}` | Get the leave balance for a specific employee and leave type. | [get_admin_leave_balance_by_id.md](./get_admin_leave_balance_by_id.md) |
| `GET` | `/admin/leave/amendments/pending` | Get all pending leave amendment requests awaiting admin review. | [get_admin_leave_amendments_pending.md](./get_admin_leave_amendments_pending.md) |
| `PUT` | `/admin/leave/amendments/{amendment_id}/approve` | Approve a pending leave amendment request. For `cancel` amendments, the original | [put_admin_leave_amendments_by_id_approve.md](./put_admin_leave_amendments_by_id_approve.md) |
| `PUT` | `/admin/leave/amendments/{amendment_id}/reject` | Reject a pending leave amendment request. The original leave request remains unc | [put_admin_leave_amendments_by_id_reject.md](./put_admin_leave_amendments_by_id_reject.md) |
| `GET` | `/admin/leave/amendments/{leave_request_id}` | Get all amendments for a specific leave request (admin view, no ownership restri | [get_admin_leave_amendments_by_id.md](./get_admin_leave_amendments_by_id.md) |
| `GET` | `/admin/leave/entitlements` | List all leave entitlements with optional filtering and pagination. | [get_admin_leave_entitlements.md](./get_admin_leave_entitlements.md) |
| `GET` | `/admin/leave/entitlements/employee/{employee_username}` | Get all leave entitlements for a specific employee. | [get_admin_leave_entitlements_employee_by_id.md](./get_admin_leave_entitlements_employee_by_id.md) |
| `GET` | `/admin/leave/entitlements/{entitlement_id}` | Get a single leave entitlement by ID. | [get_admin_leave_entitlements_by_id.md](./get_admin_leave_entitlements_by_id.md) |
| `POST` | `/admin/leave/entitlements` | Create a new leave entitlement for a single employee. | [post_admin_leave_entitlements.md](./post_admin_leave_entitlements.md) |
| `POST` | `/admin/leave/entitlements/bulk` | Create the same leave entitlement for multiple employees at once. | [post_admin_leave_entitlements_bulk.md](./post_admin_leave_entitlements_bulk.md) |
| `PUT` | `/admin/leave/entitlements/{entitlement_id}` | Update an existing leave entitlement. All fields are optional; only provided fie | [put_admin_leave_entitlements_by_id.md](./put_admin_leave_entitlements_by_id.md) |
| `DELETE` | `/admin/leave/entitlements/{entitlement_id}` | Permanently delete a leave entitlement. | [delete_admin_leave_entitlements_by_id.md](./delete_admin_leave_entitlements_by_id.md) |
