# POST /job-applications/admin/{application_id}/reject

Reject a job application. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | No | Rejection reason |

**Response:** Updated application object with status "rejected"

**Errors:**
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application not found
