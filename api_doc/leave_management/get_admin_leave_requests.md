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
      "leave_type": "annual",
      "status": "pending",
      "leave_periods": [],
      "created_at": "datetime"
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
