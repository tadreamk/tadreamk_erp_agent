# GET /admin/leave/requests/pending


Get leave requests with `pending` status awaiting approval.

**Access control:** Whitelist `leave-management` required.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | No | Filter by leave type |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 50) |

**Response:**
```json
{
  "requests": [
    {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "employee_username": "john.doe",
      "leave_type": "annual",
      "total_days": 3.0,
      "status": "pending",
      "...": "..."
    }
  ],
  "total": 5,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`
