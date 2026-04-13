# PATCH /job-applications/{application_id}/interview-accept

Accept an interview time from admin's proposal. Candidate only. Sends a confirmation email with meeting details.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string | The application's unique identifier |

**Auth:** Requires authentication. Must be the candidate on the application.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| selected_time | string | Yes | Selected interview time from admin's proposal (UTC datetime string) |

**Response:** `200 OK` — Full application object (`JobApplicationResponse`)

**Errors:**
- `400` — Invalid application_id format
- `403` — Access denied
- `404` — Application not found
- `500` — Failed to accept interview time
