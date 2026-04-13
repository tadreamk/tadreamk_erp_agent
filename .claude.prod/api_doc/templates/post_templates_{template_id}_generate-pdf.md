# POST /templates/{template_id}/generate-pdf

Generate a PDF from a template with provided field values. For static PDF templates, returns the existing PDF URL. Requires `templates` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | UUID | The template's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes | Map of template field keys to values |

**Response:**
```json
{
  "template_id": "uuid",
  "template_type": "dynamic",
  "pdf_url": null,
  "pdf_content_base64": null,
  "preview_html": "<html>...</html>"
}
```

**Errors:**
- `400` — Invalid template ID format
- `401` — Not authenticated
- `403` — Not on templates whitelist
- `404` — Template not found
