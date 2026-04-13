# PUT /admin/leave/amendments/{amendment_id}/approve

Approve a leave amendment request. Requires `leave-management` whitelist. Amendment must be in `pending` status.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| amendment_id | uuid | Yes | Amendment ID |

**Response:**
```json
{
  "message": "Amendment cancel approved",
  "amendment": {
    "id": "uuid",
    "leave_request_id": "uuid",
    "amendment_type": "cancel",
    "new_leave_periods": null,
    "new_swap_work_periods": null,
    "reason": "Plans changed",
    "status": "approved",
    "requested_by": "john_doe",
    "reviewed_by": "admin_user",
    "reviewed_at": "datetime",
    "created_at": "datetime"
  }
}
```

**Errors:**
- `400` — Amendment has already been processed
- `401` — Not authenticated
- `403` — No leave-management whitelist access
- `404` — Amendment not found
