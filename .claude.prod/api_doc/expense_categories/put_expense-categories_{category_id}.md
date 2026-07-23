# PUT /expense-categories/{category_id}

Update Expense Category Route. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No |  |
| description | string | No |  |
| is_active | boolean | No |  |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "is_active": false,
  "created_at": "datetime",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_at": "datetime",
  "updated_by": "string",
  "updated_by_preferred_name": "string"
}
```

**Errors:**
- `422` — Validation Error
