# GET /admin/leave/amendments/{leave_request_id}

Get all amendments for a leave request (admin view). Requires `leave-management` whitelist.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_request_id | uuid | Yes | Leave request ID |

**Response:**
```json
[
  {
    "id": "uuid",
    "leave_request_id": "uuid",
    "amendment_type": "cancel",
    "new_leave_periods": null,
    "new_swap_work_periods": null,
    "reason": "Plans changed",
    "status": "pending",
    "requested_by": "john_doe",
    "reviewed_by": null,
    "reviewed_at": null,
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No leave-management whitelist access
