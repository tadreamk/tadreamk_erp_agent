# PUT /job-applications/{application_id}/exercise-urls

Submit exercise submission URLs for an application. Requires authentication (application owner).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| exercise_github_url | string | No | GitHub repository URL for exercise submission (max 2048 chars) |
| exercise_report_url | string | No | Report/document URL for exercise submission (max 2048 chars) |

**Response:** Updated application object

**Errors:**
- `401` — Not authenticated
- `403` — Access denied
- `404` — Application not found
