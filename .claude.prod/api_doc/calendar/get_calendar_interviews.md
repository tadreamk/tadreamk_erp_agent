# GET /calendar/interviews

Get confirmed interviews within a date range for calendar display.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start_date | date | Yes | Start of range (YYYY-MM-DD) |
| end_date | date | Yes | End of range (YYYY-MM-DD) |

**Response:**
```json
{
  "events": [
    {
      "id": "uuid",
      "candidate": "John Smith",
      "start_time": "2026-03-20T10:00:00",
      "date": "2026-03-20",
      "event_type": "interview",
      "interviewers": ["alice", "bob"],
      "status": "interview_confirmed"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
