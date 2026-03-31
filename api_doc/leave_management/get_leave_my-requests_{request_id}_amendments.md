# GET /leave/my-requests/{request_id}/amendments

Get amendments for a leave request (employee view). Requires authentication. Only own requests can be accessed.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| request_id | uuid | Yes | Leave request ID |

**Response:**
```json
[
  {
    "id": "uuid",
    "leave_request_id": "uuid",
    "amendment_type": "cancel",
    "reason": "Plans changed",
    "status": "pending",
    "requested_by": "john_doe",
    "reviewed_by": null,
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to view amendments for this request
- `404` — Leave request not found
