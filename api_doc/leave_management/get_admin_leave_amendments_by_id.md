# GET /admin/leave/amendments/{leave_request_id}


Get all amendments for a specific leave request (admin view, no ownership restriction).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| leave_request_id | UUID | Leave request ID |

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
    "status": "approved",
    "requested_by": "john.doe",
    "reviewed_by": "admin.user",
    "reviewed_at": "2026-03-12T09:00:00+00:00",
    "created_at": "2026-03-11T10:00:00+00:00"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`

---

## 35. Leave Entitlement (Admin)

Administrative endpoints for managing employee leave entitlements (allocations). Controls how many days of each leave type an employee is granted for a given date range.

**Prefix:** `/admin/leave/entitlements`

**Access control:** Admin authentication required for all endpoints.
