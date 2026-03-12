# GET /leave/my-requests


Get the current user's leave requests with optional filtering and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status_filter | string | No | Filter by status (`pending`, `approved`, `rejected`, `cancelled`) |
| leave_type | string | No | Filter by leave type (`annual`, `sick`, `no_pay`, `maternal`, `swap_off`, `swap_work`, `remote_work`) |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 50) |

**Response:**
```json
{
  "requests": [
    {
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
      "updated_at": null,
      "has_pending_amendment": false
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Employee record not found for current user
