# POST /templates/{template_id}/generate-preview-pdf

Generate a PDF preview from pre-rendered HTML. Uploads the resulting PDF to GCS `tmp/` folder and returns the public URL. No database write — file is ephemeral.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | string | The template's unique identifier |

**Auth:** Requires `templates` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| html_content | string | Yes | Pre-rendered HTML string to convert to PDF |

**Response:** `200 OK`
```json
{
  "pdf_url": "https://storage.googleapis.com/.../tmp/template-slug_123456.pdf",
  "template_id": "uuid"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on templates whitelist
- `404` — Template not found
