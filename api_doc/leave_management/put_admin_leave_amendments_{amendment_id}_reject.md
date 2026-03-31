# PUT /admin/leave/amendments/{amendment_id}/reject

Reject a leave amendment request. Requires `leave-management` whitelist. Amendment must be in `pending` status.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| amendment_id | uuid | Yes | Amendment ID |

**Response:**
```json
{
  "message": "Amendment rejected",
  "amendment": {
    "id": "uuid",
    "status": "rejected",
    "reviewed_by": "admin_user"
  }
}
```

**Errors:**
- `400` — Amendment has already been processed
- `401` — Not authenticated
- `403` — No leave-management whitelist access
- `404` — Amendment not found
