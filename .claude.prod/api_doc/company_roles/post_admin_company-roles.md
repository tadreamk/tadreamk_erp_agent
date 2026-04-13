# POST /admin/company-roles

Assign a role to a user. Requires `company-roles` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes | Username of the employee |
| role_title | string | Yes | Role title to assign |
| role_description | string | No | Optional description |

**Response:**
```json
{
  "company_role": {
    "id": "uuid",
    "username": "alice",
    "role_title": "HR Manager",
    "role_description": "string",
    "is_active": true,
    "created_by": "string",
    "created_at": "datetime"
  },
  "was_created": true
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No company-roles whitelist access
