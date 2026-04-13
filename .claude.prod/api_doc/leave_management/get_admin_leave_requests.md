# GET /admin/leave/requests

List all leave requests with optional filters. Requires `leave-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status_filter | string | No | Filter by status (pending, approved, rejected, cancelled) |
| leave_type | string | No | Filter by leave type |
| from_date | date | No | Filter by start date |
| to_date | date | No | Filter by end date |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 50) |

**Response:**
```json
{
  "requests": [
    {
      "id": "uuid",
      "employee_username": "alice",
      "manager_username": "manager_user",
      "leave_type": "annual",
      "leave_periods": [],
      "swap_work_periods": [],
      "total_days": 5.0,
      "leave_reason": "Family vacation",
      "supporting_document_urls": [],
      "status": "pending",
      "reviewed_by_username": null,
      "reviewed_at": null,
      "created_at": "datetime",
      "updated_at": "datetime",
      "has_pending_amendment": false
    }
  ],
  "total": 20,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No leave-management whitelist access
