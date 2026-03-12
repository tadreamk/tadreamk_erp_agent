# POST /templates/{template_id}/preview


Preview a template with field values. Returns rendered HTML for dynamic templates or a PDF URL for static PDF templates.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| template_id | string (UUID) | Yes | Template unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes | Key-value map of field_key to value |

```json
{
  "field_values": {
    "employee_name": "John Doe",
    "start_date": "2026-03-01"
  }
}
```

**Response (dynamic template):**
```json
{
  "template_id": "uuid",
  "template_type": "dynamic",
  "preview_html": "<!DOCTYPE html><html>...</html>",
  "pdf_url": null
}
```

**Response (PDF template):**
```json
{
  "template_id": "uuid",
  "template_type": "pdf",
  "preview_html": null,
  "pdf_url": "https://storage.googleapis.com/bucket/template.pdf"
}
```

**Errors:**
- `400` — Invalid template ID format
- `401` — Not authenticated
- `403` — No templates whitelist access
- `404` — Template not found
