# PATCH /job-applications/admin/{application_id}/status


Update the status of an application. Used to manually move applications through the pipeline.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string (UUID) | Application ID |

**Request Body (JSON):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| status | string | Yes | New application status (one of the `ApplicationStatus` enum values) |

**Example Request:**
```json
{
  "status": "exercise_assigned"
}
```

**Response (200):** Updated `JobApplicationResponse` object.

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid application ID format |
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
| 404 | Application not found |
| 500 | Failed to update application status |
