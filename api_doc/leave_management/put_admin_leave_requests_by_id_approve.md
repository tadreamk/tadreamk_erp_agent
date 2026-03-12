# PUT /admin/leave/requests/{request_id}/approve


Approve a pending leave request. Sends an approval notification and email to the employee. Also sends day-swap approval emails when the request includes swap work periods.

**Access control:** Whitelist `leave-management` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | Leave request ID (must have `pending` status) |

**Response:**
```json
{
  "message": "Leave request approved successfully",
  "leave_request": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "status": "approved",
    "reviewed_by_username": "admin.user",
    "reviewed_at": "2026-03-11T14:30:00+00:00",
    "...": "..."
  }
}
```

**Errors:**
- `400` — Request has already been approved/rejected/cancelled
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`
- `404` — Leave request not found
