# POST /payslip-workflow/batch

Create payslips for multiple employees at once. Skips employees that already have a payslip for the given month. Also creates linked expense records. Requires `payslip` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_usernames | list[string] | Yes | List of employee usernames |
| payroll_month | string | Yes | Payroll month (e.g. "2024-01") |
| template_id | UUID | Yes | Template to use for the payslips |

**Response:**
```json
{
  "created_count": 5,
  "payslip_ids": ["uuid1", "uuid2"],
  "message": "Created 5 payslips"
}
```

**Errors:**
- `400` — Template not found, or employee not found / has no contract
- `401` — Not authenticated
- `403` — Not on payslip whitelist
