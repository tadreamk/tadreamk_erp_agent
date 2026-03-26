# PATCH /job-applications/{application_id}/exercise-urls

Submit exercise submission URLs for an application. Requires authentication (application owner).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| exercise_urls | list[string] | Yes | URLs of submitted exercise materials |

**Response:** Updated application object

**Errors:**
- `401` — Not authenticated
- `403` — Access denied
- `404` — Application not found
