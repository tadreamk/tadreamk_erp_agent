# POST /templates/{template_id}/preview

Preview a template with provided field values. Returns rendered HTML for dynamic templates, or the PDF URL for static PDF templates. Requires `templates` whitelist access.

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
  "preview_html": "<html>...</html>",
  "pdf_url": null
}
```

**Errors:**
- `400` — Invalid template ID format
- `401` — Not authenticated
- `403` — Not on templates whitelist
- `404` — Template not found
