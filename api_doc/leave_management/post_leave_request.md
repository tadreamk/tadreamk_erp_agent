# POST /leave/request

Submit a new leave request. Requires authentication. Validates balance for annual/sick leave.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| leave_type | string | Yes | Leave type: `annual`, `sick`, `no_pay`, `maternal`, `swap_off`, `swap_work`, `remote_work` |
| leave_periods | list | Yes | List of leave date periods |
| leave_reason | string | No | Reason for leave |
| manager_username | string | No | Manager to notify (defaults to employee's manager) |
| swap_work_periods | list | No | Work periods to swap (for swap leave) |

Each `leave_period`:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| start_date | date | Yes | Period start date |
| start_apm | string | No | `AM` (default) or `PM` — start half-day marker |
| end_date | date | Yes | Period end date (must be >= start_date) |
| end_apm | string | No | `AM` or `PM` (default) — end half-day marker |

**Response:**
```json
{
  "message": "Leave request submitted successfully",
  "leave_request": { "...leave request..." }
}
```

**Errors:**
- `400` — Cannot request leave for past dates, or insufficient balance (annual), or exceeded monthly sick leave limit
- `401` — Not authenticated
- `403` — Not an employee

**Sick leave monthly limit error example:**
```json
{
  "detail": "Exceeded monthly paid sick leave limit of 4 days for March 2026. You have already used 3 days this month and requested 2 more (total: 5). Please apply for no-pay leave for the additional days."
}
```
