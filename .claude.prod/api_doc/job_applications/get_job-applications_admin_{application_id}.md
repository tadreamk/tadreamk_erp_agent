# GET /job-applications/admin/{application_id}

Get a specific application by ID. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Response:** Full application object

**Errors:**
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application not found
