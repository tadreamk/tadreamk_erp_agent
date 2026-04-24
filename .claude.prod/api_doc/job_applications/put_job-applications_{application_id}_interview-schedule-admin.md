# PUT /job-applications/{application_id}/interview-schedule-admin

Set the interview schedule for a job application. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| time_slots | list[string] | Yes | List of proposed interview times (UTC datetime strings, 1-5 slots) |
| duration_minutes | integer | No | Interview duration in minutes (default: 30) |

**Response:** Updated application object

**Errors:**
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application not found
