# GET /templates/{template_id}/download-pdf


Download PDF for a template. For PDF templates, returns the direct PDF URL. For dynamic templates, instructs the client to use the `POST /generate-pdf` endpoint instead.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| template_id | string (UUID) | Yes | Template unique identifier |

**Response (PDF template):**
```json
{
  "template_id": "uuid",
  "template_type": "pdf",
  "pdf_url": "https://storage.googleapis.com/bucket/template.pdf",
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
- `403` — No templates whitelist access
- `404` — Template not found
