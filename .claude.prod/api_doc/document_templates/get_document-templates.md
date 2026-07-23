# GET /document-templates

List Document Templates. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | DocumentTemplateCategoryEnum | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "templates": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "category": "string",
      "fields": [
        {
          "field_key": {},
          "title": {},
          "data_type": {},
          "description": {},
          "options": {},
          "input_by_role": {},
          "input_by_username": {},
          "section": {},
          "group": {},
          "default_value": {}
        }
      ],
      "pdf_url": "string",
      "is_active": false,
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
