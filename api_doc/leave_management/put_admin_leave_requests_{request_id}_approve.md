# PUT /admin/leave/requests/{request_id}/approve

Approve a leave request. Requires `leave-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | The leave request's unique identifier |

**Response:**
```json
{
  "message": "Leave request approved successfully",
  "leave_request": { "...leave request with status: approved..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No leave-management whitelist access
- `404` — Leave request not found
