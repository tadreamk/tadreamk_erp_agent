# GET /employees/

List Employees. Requires `)
    entries, total = employee_crud.search_employees(
        db, search=search, include_inactive=include_inactive, page=page, limit=limit
    )
    audit_names = preferred_names(db, (u for e in entries for u in (e.created_by, e.updated_by)))
    return {
        ` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No |  |
| include_inactive | boolean | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "uuid",
      "username": "string",
      "work_email": "string",
      "preferred_name": "string",
      "manager_username": "string",
      "manager_preferred_name": "string",
      "is_active": false,
      "created_at": "datetime",
      "created_by": "string",
      "created_by_preferred_name": "string",
      "updated_at": "datetime",
      "updated_by": "string",
      "updated_by_preferred_name": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
