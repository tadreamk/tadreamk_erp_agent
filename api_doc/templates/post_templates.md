# POST /templates

Create or update a template by ID. Admin only.

If a template with the given ID already exists, it will be updated. Otherwise, a new template is created.

**Authentication:** Admin or moderator role required.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string (uuid) | Yes | Template UUID |
| title | string | Yes | Template title |
| description | string | No | Template description |
| category | string | Yes | Template category (e.g., `contract`, `finance`, `onboarding`) |
| fields | array[object] | Yes | List of field definitions |
| is_active | boolean | No | Whether template is active (default: true) |
| version | integer | No | Template version number (default: 1) |

**Field definition object:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_key | string | Yes | Unique field identifier |
| title | string | Yes | Display label |
| data_type | string | Yes | Input type: `text`, `textarea`, `number`, `date`, `select`, `tel`, `signature` |
| section | string | No | Section grouping |
| input_by_role | string | Yes | Role responsible: `hr`, `employee`, `ceo` |
| options | array[string] | No | Options for `select` type |
| default_value | string | No | Default field value |

**Example Request:**
```json
{
  "id": "c0000001-0000-4000-8000-000000000001",
  "title": "Full-time Employment Contract",
  "description": "Standard full-time employment contract.",
  "category": "contract",
  "is_active": true,
  "version": 1,
  "fields": [
    {
      "field_key": "candidate_title",
      "title": "Title",
      "data_type": "select",
      "section": "Employee Details",
      "input_by_role": "employee",
      "options": ["Mr", "Ms", "Mrs", "Dr", "Prof"]
    }
  ]
}
```

**Response:** Returns the created/updated template object (same shape as `GET /templates/{template_id}`).

**Errors:**
- `401` — Not authenticated
- `403` — Not admin/moderator
- `400` — Invalid template ID format
