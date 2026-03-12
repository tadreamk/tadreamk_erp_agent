# GET /calendar/interviews


Get confirmed interviews for calendar display within a date range.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start_date | date | Yes | Range start date (YYYY-MM-DD) |
| end_date | date | Yes | Range end date (YYYY-MM-DD) |

**Included interview statuses:** `interview_confirmed`, `interview_finished`, `accepted`, `rejected`

**Response:**
```json
{
  "events": [
    {
      "id": "770e8400-e29b-41d4-a716-446655440000",
      "candidate": "Jane Smith",
      "start_time": "2026-03-15T14:00:00",
      "date": "2026-03-15",
      "event_type": "interview",
      "interviewers": ["john.doe", "admin"],
      "status": "interview_confirmed"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Employee access required

---

## 57. Calendar (Admin)

Admin calendar endpoints with expanded access. Requires admin/moderator role and `calendar` whitelist access.

**Access control:** Admin or moderator role + `calendar` whitelist entry required.
