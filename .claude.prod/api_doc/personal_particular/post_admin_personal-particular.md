# POST /admin/personal-particular

Create a new personal particular record for a specified user (HR only). Links the record to the employee if they exist. Requires `personal-particulars` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes | Username of the employee |

**Request Body:** Key-value map of personal particular fields (same fields as self-service POST)

**Response:** `201 Created`
```json
{
  "message": "Personal particular created",
  "personal_particular": { "...full personal particular object..." }
}
```

**Errors:**
- `400` — `username` query parameter is required; or record already exists for this username
- `401` — Not authenticated
- `403` — Not on personal-particulars whitelist
