# Payslip Workflow API

Base prefix: `/payslip-workflow`

Authentication: HR/Finance endpoints require `payslip` whitelist access. Employee endpoints require authentication. GET `/{workflow_id}` is accessible by the employee, HR, or CEO.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/payslip-workflow/employees` | Get active employees for payslip batch creation (HR) |
| POST | `/payslip-workflow/batch` | Create payslips for multiple employees at once (HR) |
| GET | `/payslip-workflow` | List all payslip workflows (HR) |
| GET | `/payslip-workflow/{workflow_id}` | Get payslip workflow details |
| PUT | `/payslip-workflow/{workflow_id}` | Update payslip field values (HR) |
| DELETE | `/payslip-workflow/{workflow_id}` | Soft delete a payslip workflow (HR) |
| GET | `/payslip-workflow/my-payslips` | Get payslips for the authenticated employee |
| POST | `/payslip-workflow/{workflow_id}/sign` | Employee signs/acknowledges a payslip |
| POST | `/payslip-workflow/{workflow_id}/confirm` | Confirm payslip and send to CEO for approval (HR) |
| POST | `/payslip-workflow/{workflow_id}/reject` | Finance rejects payslip with reason (Finance) |

## Endpoint Documentation

- [GET /payslip-workflow/employees](get_payslip-workflow_employees.md)
- [POST /payslip-workflow/batch](post_payslip-workflow_batch.md)
- [GET /payslip-workflow](get_payslip-workflow.md)
- [GET /payslip-workflow/{workflow_id}](get_payslip-workflow_{workflow_id}.md)
- [PUT /payslip-workflow/{workflow_id}](put_payslip-workflow_{workflow_id}.md)
- [DELETE /payslip-workflow/{workflow_id}](delete_payslip-workflow_{workflow_id}.md)
- [GET /payslip-workflow/my-payslips](get_payslip-workflow_my-payslips.md)
- [POST /payslip-workflow/{workflow_id}/sign](post_payslip-workflow_{workflow_id}_sign.md)
- [POST /payslip-workflow/{workflow_id}/confirm](post_payslip-workflow_{workflow_id}_confirm.md)
- [POST /payslip-workflow/{workflow_id}/reject](post_payslip-workflow_{workflow_id}_reject.md)
