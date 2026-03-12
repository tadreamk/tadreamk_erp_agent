# PUT /leave/my-requests/{request_id}/cancel


Cancel a pending leave request. Only requests with `pending` status can be cancelled.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | Leave request ID |

**Response:**
```json
{
  "message": "Leave request cancelled",
  "leave_request": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "status": "cancelled",
    "...": "..."
  }
}
```

**Errors:**
- `400` — Cannot cancel request with status other than `pending`
- `401` — Not authenticated
- `403` — Not authorized to cancel this request
- `404` — Leave request not found
