# POST /job-applications/admin/{application_id}/accept

Accept a job application. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Response:** Updated application object with status "accepted"

**Errors:**
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application not found
