# GET /calendar/team


Get team calendar with approved leaves for a given month. Defaults to the current month if no parameters are provided.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| year | int | No | Current year | Calendar year |
| month | int | No | Current month | Calendar month (1-12) |
| department | string | No | null | Filter by department |
| leave_type | string | No | null | Filter by leave type |

**Leave type values:** `annual`, `sick`, `no_pay`, `maternal`, `swap_off`, `swap_work`, `remote_work`

**Response:**
```json
{
  "year": 2026,
  "month": 3,
  "start_date": "2026-03-01",
  "end_date": "2026-03-31",
  "events": [
    {
      "id": "leave-550e8400-2026-03-15",
      "title": "(AM) John Doe",
      "date": "2026-03-15",
      "event_type": "leave",
      "leave_type": "annual",
      "is_full_day": false,
      "period": "AM",
      "color": "#3b82f6",
      "employee_username": "john.doe",
      "employee_name": "John Doe",
      "department": "Engineering"
    }
  ],
  "departments": ["Engineering", "Design", "HR"]
}
```

**Leave type color mapping:**
| Leave Type | Color |
|------------|-------|
| annual | `#3b82f6` (Blue) |
| sick | `#f59e0b` (Amber) |
| no_pay | `#6b7280` (Gray) |
| maternal | `#ec4899` (Pink) |
| swap_off | `#8b5cf6` (Purple) |
| swap_work | `#06b6d4` (Cyan) |
| remote_work | `#ef4444` (Red) |

**Errors:**
- `400` — Invalid month
- `401` — Not authenticated
- `403` — Employee access required
