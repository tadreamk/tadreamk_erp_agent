# DELETE /company-roles/{role_title}

Revoke Role. Requires `)
    assert_known_role_title(role_title)

    entry = company_role_service.revoke_role(db, role_title=role_title, caller=user.username)
    if entry is None:
        raise HTTPException(status_code=404, detail=f` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| role_title | string |  |

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
