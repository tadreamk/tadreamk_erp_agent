# GET /admin/leave/calendar


Get employees who are on approved leave for a specific date.

**Access control:** Whitelist `leave-management` required.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| target_date | date | No | Date to check (YYYY-MM-DD, default: today) |

**Response:**
```json
[
  {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "employee_username": "john.doe",
    "leave_type": "annual",
    "total_days": 3.0,
    "status": "approved",
    "...": "..."
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`
