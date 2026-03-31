# GET /admin/leave/amendments/pending

Get pending leave amendment requests. Requires `leave-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 50) |

**Response:**
```json
{
  "amendments": [
    {
      "id": "uuid",
      "leave_request_id": "uuid",
      "amendment_type": "cancel",
      "reason": "Plans changed",
      "status": "pending",
      "requested_by": "john_doe",
      "created_at": "datetime"
    }
  ],
  "total": 10,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No leave-management whitelist access
