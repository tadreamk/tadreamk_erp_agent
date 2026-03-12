# POST /admin/company-roles


Assign a role to a user. If the role title does not already exist, it will be created.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes | Username to assign the role to (1-100 chars) |
| role_title | string | Yes | Role title to assign (1-50 chars) |
| role_description | string | No | Optional description for the role |

**Request Example:**
```json
{
  "username": "john.doe",
  "role_title": "head_of_hr",
  "role_description": "Head of Human Resources"
}
```

**Response (201):**
```json
{
  "company_role": {
    "id": "uuid",
    "username": "john.doe",
    "role_title": "head_of_hr",
    "role_description": "Head of Human Resources",
    "is_active": true,
    "created_at": "2025-06-01T00:00:00+00:00",
    "created_by": "admin.user"
  },
  "was_created": true
}
```

The `was_created` field indicates whether this is a new assignment (`true`) or a reactivated existing one (`false`).
