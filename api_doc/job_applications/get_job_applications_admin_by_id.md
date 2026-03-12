# GET /job-applications/admin/{application_id}


Get a specific application by ID (admin/moderator only). Uses `require_admin_auth` dependency directly.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string (UUID) | Application ID |

**Response (200):** Same `JobApplicationResponse` schema as Section 7.

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid application ID format |
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
| 404 | Application not found |
