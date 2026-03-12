# GET /admin/company-roles/roles/{role_title}/users


List all active usernames assigned to a specific role.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| role_title | string | Yes | Role title to look up |

**Response:**
```json
{
  "usernames": ["john.doe", "jane.smith"],
  "role_title": "head_of_hr",
  "total": 2
}
```

**Errors:**
- `404` -- Role '{role_title}' not found
