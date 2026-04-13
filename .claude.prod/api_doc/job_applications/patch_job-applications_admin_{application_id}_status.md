# PATCH /job-applications/admin/{application_id}/status

Update an application's status. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| status | string | Yes | New application status |

**Response:** Updated application object

**Errors:**
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application not found
- `500` — Failed to update status
