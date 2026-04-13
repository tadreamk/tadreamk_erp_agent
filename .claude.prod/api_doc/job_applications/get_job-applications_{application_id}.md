# GET /job-applications/{application_id}

Get a specific application by ID. Access requires ownership or admin/whitelist access. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Response:** Full application object

**Errors:**
- `401` — Not authenticated
- `403` — Access denied
- `404` — Application not found
