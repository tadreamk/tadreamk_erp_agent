# PUT /employees/company-roles/{role_title}


Update username assignment for a company role. Revokes all existing active assignments for the given role title, then assigns the new user.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| role_title | string | Yes | The role title to reassign |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes | Username to assign (1-100 chars) |

**Request Example:**
```json
{
  "username": "jane.smith"
}
```

**Response:**
```json
{
  "message": "Role 'head_of_hr' assigned to 'jane.smith'",
  "role": {
    "id": "uuid",
    "username": "jane.smith",
    "role_title": "head_of_hr"
  }
}
```
