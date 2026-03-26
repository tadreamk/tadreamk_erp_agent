# GET /templates

List all templates with optional filtering. Returns active templates by default. Requires `templates` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | string | No | Filter by category |
| is_active | boolean | No | Filter by active status (default: true) |
| skip | integer | No | Pagination offset (default: 0) |
| limit | integer | No | Max results (default: 100) |

**Response:**
```json
{
  "templates": [
    {
      "id": "uuid",
      "name": "string",
      "category": "string",
      "is_active": true,
      "template_type": "dynamic"
    }
  ],
  "total": 10
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on templates whitelist
