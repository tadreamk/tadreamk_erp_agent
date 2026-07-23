# GET /document-templates/{template_id}

Get Document Template. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "category": "string",
  "fields": [
    {
      "field_key": "string",
      "title": "string",
      "data_type": "string",
      "description": "string",
      "options": [
        {}
      ],
      "input_by_role": "string",
      "input_by_username": "string",
      "section": "string",
      "group": "string",
      "default_value": {}
    }
  ],
  "pdf_url": "string",
  "is_active": false,
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors:**
- `422` — Validation Error
