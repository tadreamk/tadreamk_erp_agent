# PUT /employees/company-roles/{role_title}

Update the user assigned to a company role (replaces existing assignment). Requires `employees` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| role_title | string | The role title to update |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes | Username to assign to the role |

**Response:**
```json
{
  "message": "Role 'HR Manager' assigned to 'alice'",
  "role": {
    "id": "uuid",
    "username": "alice",
    "role_title": "HR Manager"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No employees whitelist access
