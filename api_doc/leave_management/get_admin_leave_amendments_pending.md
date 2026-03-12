# GET /admin/leave/amendments/pending


Get all pending leave amendment requests awaiting admin review.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 50) |

**Response:**
```json
{
  "amendments": [
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
  ],
  "total": 3,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`
