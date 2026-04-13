# GET /admin/company-roles

List all company role assignments. Requires `company-roles` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | int | No | Max results (default: 100) |
| offset | int | No | Offset (default: 0) |

**Response:**
```json
{
  "company_roles": [
    {
      "id": "uuid",
      "username": "alice",
      "role_title": "HR Manager",
      "role_description": "string",
      "is_active": true,
      "created_by": "string",
      "created_at": "datetime"
    }
  ],
  "total": 10
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No company-roles whitelist access
