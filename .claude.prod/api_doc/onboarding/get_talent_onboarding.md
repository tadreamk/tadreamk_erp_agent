# GET /talent/onboarding

Get My Onboarding. Requires authentication.

**Response:**
```json
{
  "workflow": {
    "id": "uuid",
    "talent_email": "string",
    "talent_username": "string",
    "talent_preferred_name": "string",
    "hr_username": "string",
    "hr_preferred_name": "string",
    "ceo_username": "string",
    "ceo_preferred_name": "string",
    "status": "string",
    "talent_submitted_at": "datetime",
    "sent_to_ceo_at": "datetime",
    "cancel_reason": "string",
    "is_active": false,
    "created_at": "datetime",
    "updated_at": "datetime",
    "documents": [
      {
        "id": {},
        "onboarding_id": {},
        "template_id": {},
        "template_name": {},
        "document_type": {},
        "pdf_url": {},
        "onedrive_url_employee": {},
        "onedrive_url_admin": {},
        "field_values": {},
        "fields": {},
        "is_locked": {},
        "created_at": {},
        "updated_at": {}
      }
    ]
  },
  "workflows": [
    {
      "id": "uuid",
      "talent_email": "string",
      "talent_username": "string",
      "talent_preferred_name": "string",
      "hr_username": "string",
      "hr_preferred_name": "string",
      "ceo_username": "string",
      "ceo_preferred_name": "string",
      "status": "string",
      "talent_submitted_at": "datetime",
      "sent_to_ceo_at": "datetime",
      "is_active": false,
      "created_at": "datetime",
      "updated_at": "datetime",
      "document_count": 0
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
