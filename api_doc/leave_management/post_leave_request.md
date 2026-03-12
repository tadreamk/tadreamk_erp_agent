# POST /leave/request


Submit a new leave request with one or more date periods. For `annual` and `sick` leave types, the employee's available balance is checked before submission. Past dates are not allowed. For `swap_off` leave, swap work periods must be provided and their total duration must equal the leave duration.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| leave_type | string | Yes | One of: `annual`, `sick`, `no_pay`, `maternal`, `swap_off`, `swap_work`, `remote_work` |
| leave_periods | array | Yes | At least one period object (see below) |
| swap_work_periods | array | No | Required for `swap_off` leave; swap work period objects |
| leave_reason | string | No | Reason for leave |
| manager_username | string | No | Override approving manager (defaults to employee's assigned manager) |

**Leave period object:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| start_date | date | Yes | Start date (YYYY-MM-DD), must not be in the past |
| start_apm | string | No | `AM` or `PM` (default: `AM`) |
| end_date | date | Yes | End date (YYYY-MM-DD), must be >= start_date |
| end_apm | string | No | `AM` or `PM` (default: `PM`) |

**Request example:**
```json
{
  "leave_type": "annual",
  "leave_periods": [
    {
      "start_date": "2026-04-01",
      "start_apm": "AM",
      "end_date": "2026-04-03",
      "end_apm": "PM"
    }
  ],
  "leave_reason": "Family vacation",
  "manager_username": "jane.smith"
}
```

**Response:**
```json
{
  "message": "Leave request submitted successfully",
  "leave_request": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "employee_username": "john.doe",
    "manager_username": "jane.smith",
    "leave_type": "annual",
    "leave_periods": [
      {
        "start_date": "2026-04-01",
        "start_apm": "AM",
        "end_date": "2026-04-03",
        "end_apm": "PM"
      }
    ],
    "swap_work_periods": null,
    "total_days": 3.0,
    "leave_reason": "Family vacation",
    "supporting_document_urls": [],
    "status": "pending",
    "reviewed_by_username": null,
    "reviewed_at": null,
    "created_at": "2026-03-10T08:00:00+00:00",
    "updated_at": null
  }
}
```

**Errors:**
- `400` — Cannot request leave for past dates
- `400` — Insufficient leave balance (for `annual` and `sick` types)
- `400` — `swap_work_periods` required for `swap_off` leave
- `400` — Leave duration must equal swap work duration (for `swap_off`)
- `401` — Not authenticated
- `404` — Employee record not found for current user
