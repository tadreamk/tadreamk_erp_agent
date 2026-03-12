# GET /leave/my-requests/{request_id}/amendments


Get all amendments for a specific leave request belonging to the current user.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | Leave request ID |

**Response:**
```json
[
  {
    "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
    "leave_request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "amendment_type": "cancel",
    "new_leave_periods": null,
    "new_swap_work_periods": null,
    "reason": "Plans changed",
    "status": "pending",
    "requested_by": "john.doe",
    "reviewed_by": null,
    "reviewed_at": null,
    "created_at": "2026-03-11T10:00:00+00:00"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to view amendments for this request
- `404` — Leave request not found

---

## 33. Leave (Admin)

Administrative endpoints for managers and HR to view, filter, approve, and reject leave requests. All endpoints require `leave-management` whitelist access unless otherwise noted.

**Prefix:** `/admin/leave`
