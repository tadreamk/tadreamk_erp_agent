# GET /templates/{template_id}

Get a template by ID. Requires `templates` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | UUID | The template's unique identifier |

**Response:** Template object with fields and structure

**Errors:**
- `400` — Invalid template ID format
- `401` — Not authenticated
- `403` — Not on templates whitelist
- `404` — Template not found
