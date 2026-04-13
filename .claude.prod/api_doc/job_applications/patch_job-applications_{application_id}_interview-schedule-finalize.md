# PATCH /job-applications/{application_id}/interview-schedule-finalize

Finalize the interview schedule for a job application. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| selected_time | string | Yes | Selected interview time from proposed slots (UTC datetime string) |

**Response:** Updated application object with confirmed schedule

**Errors:**
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application not found
