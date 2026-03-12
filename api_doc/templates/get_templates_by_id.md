# GET /templates/{template_id}


Get a single template by ID.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| template_id | string (UUID) | Yes | Template unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "title": "Employment Contract",
  "description": "Standard employment contract template",
  "category": "onboarding",
  "fields": [],
  "pdf_url": null,
  "is_active": true,
  "version": 1,
  "created_at": "2026-01-10T08:00:00+00:00",
  "updated_at": "2026-01-10T08:00:00+00:00"
}
```

**Errors:**
- `400` — Invalid template ID format
- `401` — Not authenticated
- `403` — No templates whitelist access
- `404` — Template not found
