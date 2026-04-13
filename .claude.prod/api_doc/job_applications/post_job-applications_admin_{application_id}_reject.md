# POST /job-applications/admin/{application_id}/reject

Reject a job application. Requires admin or moderator role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | UUID | The application's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | Yes | Rejection reason (min 1 char) |

**Response:**
```json
{
  "message": "Candidate rejected",
  "application": { "...application object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not admin or moderator
- `404` — Application not found
