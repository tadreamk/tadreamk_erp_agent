# GET /admin/leave/stats

Get leave dashboard statistics. Requires `leave-management` whitelist.

**Response:**
```json
{
  "pending_requests": 5,
  "on_leave_today": 3,
  "swap_pending": 2
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No leave-management whitelist access
