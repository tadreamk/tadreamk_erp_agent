# GET /employees/{username}

Get Employee. Requires `)
    entry = get_employee_or_404_by_username(db, username)
    audit_names = resolve_audit_pair_names(
        db,
        created_by=entry.created_by,
        updated_by=entry.updated_by,
    )
    return APIResponse(
        success=True,
        message=` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string |  |

**Response:**
```json
{
  "success": false,
  "message": "string",
  "data": {}
}
```

**Errors:**
- `422` — Validation Error
