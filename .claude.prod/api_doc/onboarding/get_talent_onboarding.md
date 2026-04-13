# GET /talent/onboarding

Get talent's active onboarding workflows with documents.

**Auth:** Requires authentication. Matches workflows by the authenticated user's email.

**Response:** `200 OK`
```json
{
  "workflow": {
    "id": "uuid",
    "talent_email": "talent@example.com",
    "talent_username": "string",
    "hr_username": "string",
    "ceo_username": "string",
    "status": "talent_input",
    "documents": [],
    "user_role": "talent",
    "is_active": true,
    "talent_submitted_at": null,
    "sent_to_ceo_at": null,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": null
  },
  "workflows": []
}
```

If no active workflows:
```json
{
  "message": "No onboarding found",
  "workflow": null,
  "workflows": []
}
```

**Errors:**
- `401` — Not authenticated
