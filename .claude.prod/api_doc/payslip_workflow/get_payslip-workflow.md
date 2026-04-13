# GET /payslip-workflow

List all payslip workflows (HR view). Requires `payslip` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| payroll_month | string | No | Filter by payroll month (e.g. "2024-01") |
| employee_username | string | No | Filter by employee username |
| limit | integer | No | Max results (default: 100, max: 500) |
| offset | integer | No | Pagination offset (default: 0) |

**Response:** Array of payslip workflow list objects

**Errors:**
- `401` — Not authenticated
- `403` — Not on payslip whitelist
