# GET /calendar/team/range

Get team calendar events for a custom date range.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start_date | date | Yes | Start of range (YYYY-MM-DD) |
| end_date | date | Yes | End of range (YYYY-MM-DD) |
| department | string | No | Filter by department |
| leave_type | string | No | Filter by leave type |

**Response:**
```json
{
  "start_date": "2026-03-01",
  "end_date": "2026-03-31",
  "events": []
}
```

**Errors:**
- `400` — End date is before start date
- `401` — Not authenticated
- `403` — Not an employee
