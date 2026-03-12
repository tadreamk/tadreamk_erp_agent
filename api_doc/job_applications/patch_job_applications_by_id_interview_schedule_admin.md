# PATCH /job-applications/{application_id}/interview-schedule-admin


Propose interview time slots to a candidate. Updates the `interview_schedule_admin` field on the application, sets the status to `interview_negotiating`, and sends a notification email to the candidate with the proposed times.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string (UUID) | Application ID |

**Request Body (JSON):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| time_slots | string[] | Yes | List of proposed interview times in ISO 8601 UTC format (1-5 slots). Example: `"2026-04-10T14:00:00Z"` |
| duration_minutes | int | No | Interview duration in minutes (default: 30, range: 15-180) |

**Example Request:**
```json
{
  "time_slots": [
    "2026-04-10T09:00:00Z",
    "2026-04-10T14:00:00Z",
    "2026-04-11T10:00:00Z"
  ],
  "duration_minutes": 45
}
```

**Response (200):** Updated `JobApplicationResponse` object (status will be `interview_negotiating`).

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid application ID format, invalid datetime format, fewer than 1 or more than 5 time slots, or duration out of range |
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
| 404 | Application not found |
| 500 | Failed to update interview schedule |
