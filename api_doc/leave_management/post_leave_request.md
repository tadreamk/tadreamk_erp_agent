# POST /leave/request

Submit a new leave request. Requires authentication. Validates balance for annual/sick leave.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| leave_type | string | Yes | Leave type (annual, sick, no_pay, maternal, swap) |
| leave_periods | list | Yes | List of leave date periods |
| leave_reason | string | No | Reason for leave |
| manager_username | string | No | Manager to notify (defaults to employee's manager) |
| swap_work_periods | list | No | Work periods to swap (for swap leave) |

Each `leave_period`:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| start_date | date | Yes | Period start date |
| end_date | date | Yes | Period end date |
| period_type | string | No | full_day, morning, afternoon |

**Response:**
```json
{
  "message": "Leave request submitted successfully",
  "leave_request": { "...leave request..." }
}
```

**Errors:**
- `400` — Cannot request leave for past dates, or insufficient balance
- `401` — Not authenticated
- `403` — Not an employee
