# PATCH /job-applications/{application_id}/interview-schedule-admin

Set the interview schedule for a job application. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| interview_date | datetime | No | Proposed interview date/time |
| interview_location | string | No | Interview location or meeting link |
| interview_notes | string | No | Additional notes for the candidate |

**Response:** Updated application object

**Errors:**
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application not found
