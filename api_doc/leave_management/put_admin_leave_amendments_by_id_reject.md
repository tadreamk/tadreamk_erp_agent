# PUT /admin/leave/amendments/{amendment_id}/reject


Reject a pending leave amendment request. The original leave request remains unchanged. Sends a notification to the requesting employee.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| amendment_id | UUID | Amendment request ID (must have `pending` status) |

**Response:**
```json
{
  "message": "Amendment rejected",
  "amendment": {
    "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
    "leave_request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "amendment_type": "cancel",
    "new_leave_periods": null,
    "new_swap_work_periods": null,
    "reason": "Plans changed",
    "status": "rejected",
    "requested_by": "john.doe",
    "reviewed_by": "admin.user",
    "reviewed_at": "2026-03-12T09:00:00+00:00",
    "created_at": "2026-03-11T10:00:00+00:00"
  }
}
```

**Errors:**
- `400` — Amendment has already been approved/rejected
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`
- `404` — Amendment not found
