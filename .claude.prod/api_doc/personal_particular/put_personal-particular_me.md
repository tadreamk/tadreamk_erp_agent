# PUT /personal-particular/me

Update personal particular data for the authenticated user. Only the user themselves can update their record. Requires authentication.

**Request Body:** Same fields as POST (all optional, only provided fields are updated)

**Response:**
```json
{
  "message": "Personal particular updated",
  "personal_particular": { "...personal particular object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Record not found. Use POST to create.
