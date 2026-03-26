# Leave Management API

Admin prefix: `/admin/leave` (requires `leave-management` whitelist)
Employee prefix: `/leave` (requires authentication)
Entitlements admin prefix: `/admin/leave/entitlements` (requires admin/moderator)
Amendments prefixes: `/admin/leave` and `/leave`

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /admin/leave/requests | `leave-management` whitelist | List all leave requests | [get_admin_leave_requests.md](get_admin_leave_requests.md) |
| GET | /admin/leave/requests/pending | `leave-management` whitelist | List pending requests | [get_admin_leave_requests_pending.md](get_admin_leave_requests_pending.md) |
| GET | /admin/leave/stats | `leave-management` whitelist | Get leave statistics | [get_admin_leave_stats.md](get_admin_leave_stats.md) |
| GET | /admin/leave/requests/{request_id} | `leave-management` whitelist | Get request by ID | [get_admin_leave_requests_{request_id}.md](get_admin_leave_requests_{request_id}.md) |
| PUT | /admin/leave/requests/{request_id}/approve | `leave-management` whitelist | Approve a request | [put_admin_leave_requests_{request_id}_approve.md](put_admin_leave_requests_{request_id}_approve.md) |
| PUT | /admin/leave/requests/{request_id}/reject | `leave-management` whitelist | Reject a request | [put_admin_leave_requests_{request_id}_reject.md](put_admin_leave_requests_{request_id}_reject.md) |
| GET | /admin/leave/calendar | `leave-management` whitelist | Get employees on leave | [get_admin_leave_calendar.md](get_admin_leave_calendar.md) |
| GET | /admin/leave/balance/{employee_username} | `leave-management` whitelist | Get employee balance | [get_admin_leave_balance_{employee_username}.md](get_admin_leave_balance_{employee_username}.md) |
| GET | /leave/my-requests | Authenticated | Get own leave requests | [get_leave_my-requests.md](get_leave_my-requests.md) |
| GET | /leave/my-requests/{request_id} | Authenticated | Get own request by ID | [get_leave_my-requests_{request_id}.md](get_leave_my-requests_{request_id}.md) |
| POST | /leave/request | Authenticated | Submit a leave request | [post_leave_request.md](post_leave_request.md) |
| PUT | /leave/my-requests/{request_id}/cancel | Authenticated | Cancel a request | [put_leave_my-requests_{request_id}_cancel.md](put_leave_my-requests_{request_id}_cancel.md) |
| POST | /leave/my-requests/{request_id}/documents | Authenticated | Upload supporting docs | [post_leave_my-requests_{request_id}_documents.md](post_leave_my-requests_{request_id}_documents.md) |
| GET | /leave/my-balance | Authenticated | Get own leave balances | [get_leave_my-balance.md](get_leave_my-balance.md) |
| GET | /leave/my-balance/{leave_type} | Authenticated | Get balance for a type | [get_leave_my-balance_{leave_type}.md](get_leave_my-balance_{leave_type}.md) |
| GET | /leave/my-entitlements | Authenticated | Get own entitlements | [get_leave_my-entitlements.md](get_leave_my-entitlements.md) |
