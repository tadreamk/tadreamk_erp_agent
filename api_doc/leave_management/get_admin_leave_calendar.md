# GET /admin/leave/calendar

Get employees on leave for a specific date. Requires `leave-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| target_date | date | No | Date to check (default: today) |

**Response:**
```json
[
  { "...leave request for employees on that date..." }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No leave-management whitelist access
