# Company Roles API

Base prefixes:
- `/company-role`
- `/company-roles`
- `/company-roles/{role_title}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /company-role/me | Authenticated employee | Get My Roles | [get_company-role_me.md](get_company-role_me.md) |
| GET | /company-roles/ | `)
    rows = company_role_queries.list_company_roles_with_holders(db)
    return {
        ` whitelist | List Company Roles | [get_company-roles_.md](get_company-roles_.md) |
| GET | /company-roles/role-titles | `)
    rows = company_role_queries.list_company_roles_with_holders(db)
    return {
        ` whitelist | List Role Titles | [get_company-roles_role-titles.md](get_company-roles_role-titles.md) |
| DELETE | /company-roles/{role_title} | `)
    assert_known_role_title(role_title)

    entry = company_role_service.revoke_role(db, role_title=role_title, caller=user.username)
    if entry is None:
        raise HTTPException(status_code=404, detail=f` whitelist | Revoke Role | [delete_company-roles_{role_title}.md](delete_company-roles_{role_title}.md) |
| PUT | /company-roles/{role_title}/reassign | `)
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
        message=f` whitelist | Reassign Role | [put_company-roles_{role_title}_reassign.md](put_company-roles_{role_title}_reassign.md) |
