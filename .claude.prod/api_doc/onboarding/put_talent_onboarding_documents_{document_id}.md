# PUT /talent/onboarding/documents/{document_id}

Update My Document Fields. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| document_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes |  |

**Response:**
```json
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
  "cancel_reason": "string",
  "is_active": false,
  "created_at": "datetime",
  "updated_at": "datetime",
  "documents": [
    {
      "id": "uuid",
      "onboarding_id": "uuid",
      "template_id": "uuid",
      "template_name": "string",
      "document_type": "string",
      "pdf_url": "string",
      "onedrive_url_employee": "string",
      "onedrive_url_admin": "string",
      "field_values": {},
      "fields": [
        {}
      ],
      "is_locked": false,
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
