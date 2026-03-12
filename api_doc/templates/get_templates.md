# GET /templates


List all templates with optional filtering. Returns active templates by default.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | string | No | Filter by template category |
| is_active | boolean | No | Filter by active status (default: `true`) |
| skip | int | No | Number of records to skip (default: 0) |
| limit | int | No | Maximum records to return (default: 100) |

**Response:**
```json
{
  "templates": [
    {
      "id": "uuid",
      "title": "Employment Contract",
      "description": "Standard employment contract template",
      "category": "onboarding",
      "fields": [
        {
          "field_key": "employee_name",
          "title": "Employee Name",
          "description": "Full legal name",
          "data_type": "text",
          "input_by_role": "hr",
          "input_by_username": null,
          "options": null
        }
      ],
      "pdf_url": null,
      "is_active": true,
      "version": 1,
      "created_at": "2026-01-10T08:00:00+00:00",
      "updated_at": "2026-01-10T08:00:00+00:00"
    }
  ],
  "total": 12
}
```

**Field `data_type` values:** `text`, `textarea`, `number`, `date`, `email`, `phone`, `select`, `checkbox`, `file`, `signature`

**Field `input_by_role` values:** `hr`, `employee`, `manager`, `system`, etc.

**Errors:**
- `401` — Not authenticated
- `403` — No templates whitelist access
