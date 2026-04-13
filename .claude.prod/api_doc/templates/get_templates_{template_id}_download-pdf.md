# GET /templates/{template_id}/download-pdf

Download the PDF for a template. For static PDF templates, returns the PDF URL. For dynamic templates, returns instructions to use the generate-pdf endpoint. Requires `templates` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | UUID | The template's unique identifier |

**Response (static PDF):**
```json
{
  "template_id": "uuid",
  "template_type": "pdf",
  "pdf_url": "https://storage.example.com/template.pdf",
  "message": "Use the pdf_url to download the PDF"
}
```

**Response (dynamic template):**
```json
{
  "template_id": "uuid",
  "template_type": "dynamic",
  "pdf_url": null,
  "message": "Use POST /generate-pdf with field_values to generate PDF"
}
```

**Errors:**
- `400` — Invalid template ID format
- `401` — Not authenticated
- `403` — Not on templates whitelist
- `404` — Template not found
