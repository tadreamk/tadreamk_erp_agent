# POST /document-templates/{template_id}/preview-pdf

Generate Document Template Preview Pdf. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| preview_html | string | No |  |
| field_values | object | Yes |  |

**Response:**
```json
{
  "pdf_url": "string"
}
```

**Errors:**
- `422` — Validation Error
