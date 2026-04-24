# PUT /job-applications/{application_id}/exercise

Assign an exercise to a job application. Sends email notification to applicant. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| exercise_id | UUID | No | Exercise ID to assign (null to unassign) |

**Response:** Updated application object

**Errors:**
- `400` — Invalid exercise ID format
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application or exercise not found
