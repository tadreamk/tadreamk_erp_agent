# PUT /company-roles/{role_title}/reassign

Reassign Role. Requires `)
    assert_known_role_title(role_title)
    try:
        company_role_service.reassign_role(
            db,
            role_title=role_title,
            new_username=payload.username,
            caller=user.username,
        )
    except CompanyRoleCreateError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc

    rows = company_role_queries.list_company_roles_with_holders(db)
    entries = [serialize_company_role_admin_list_row(rt, cr, emp) for rt, cr, emp in rows]
    return APIResponse(
        success=True,
        message=f` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| role_title | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes |  |

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
