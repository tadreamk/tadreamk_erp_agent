# GET /admin/leave/stats


Get leave dashboard statistics: counts of pending requests, employees currently on leave, pending swap requests, and total employees.

**Access control:** Whitelist `leave-management` required.

**Response:**
```json
{
  "pending_requests": 5,
  "on_leave_today": 3,
  "swap_pending": 2,
  "total_employees": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`
