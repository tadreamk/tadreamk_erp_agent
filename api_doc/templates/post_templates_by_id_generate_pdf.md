# POST /templates/{template_id}/generate-pdf


Generate a PDF from a template with field values. For PDF templates, returns the existing PDF URL. For dynamic templates, renders HTML and converts to PDF.

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
  "pdf_url": null,
  "pdf_content_base64": null,
  "preview_html": "<!DOCTYPE html><html>...</html>"
}
```

**Response (PDF template):**
```json
{
  "template_id": "uuid",
  "template_type": "pdf",
  "pdf_url": "https://storage.googleapis.com/bucket/template.pdf",
  "pdf_content_base64": null
}
```

**Errors:**
- `400` — Invalid template ID format
- `401` — Not authenticated
- `403` — No templates whitelist access
- `404` — Template not found
