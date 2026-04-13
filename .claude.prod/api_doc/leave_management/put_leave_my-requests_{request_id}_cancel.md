# PUT /leave/my-requests/{request_id}/cancel

Cancel a pending leave request. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | The leave request's unique identifier |

**Response:**
```json
{
  "message": "Leave request cancelled",
  "leave_request": { "...leave request with status: cancelled..." }
}
```

**Errors:**
- `400` — Cannot cancel request with non-pending status
- `401` — Not authenticated
- `403` — Not authorized to cancel this request
- `404` — Leave request not found
