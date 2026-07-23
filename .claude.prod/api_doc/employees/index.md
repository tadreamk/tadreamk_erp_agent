# Employees API

Base prefixes:
- `/employee`
- `/employees`
- `/employees/{username}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /employee/colleagues | Authenticated employee | List Colleagues | [get_employee_colleagues.md](get_employee_colleagues.md) |
| GET | /employee/me | Authenticated employee | Get Me | [get_employee_me.md](get_employee_me.md) |
| GET | /employees/ | `)
    entries, total = employee_crud.search_employees(
        db, search=search, include_inactive=include_inactive, page=page, limit=limit
    )
    audit_names = preferred_names(db, (u for e in entries for u in (e.created_by, e.updated_by)))
    return {
        ` whitelist | List Employees | [get_employees_.md](get_employees_.md) |
| POST | /employees/ | `)
    if payload.manager_username and payload.manager_username == payload.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=` whitelist | Create Employee | [post_employees_.md](post_employees_.md) |
| GET | /employees/active | `)
    entries = employee_crud.list_active_employees_for_picker(db, q=q)
    return {` whitelist | List Active For Picker | [get_employees_active.md](get_employees_active.md) |
| GET | /employees/stats | `employees` whitelist | Get Stats | [get_employees_stats.md](get_employees_stats.md) |
| GET | /employees/{username} | `)
    entry = get_employee_or_404_by_username(db, username)
    audit_names = resolve_audit_pair_names(
        db,
        created_by=entry.created_by,
        updated_by=entry.updated_by,
    )
    return APIResponse(
        success=True,
        message=` whitelist | Get Employee | [get_employees_{username}.md](get_employees_{username}.md) |
| PUT | /employees/{username} | `)
    try:
        entry = employee_crud.update_employee(
            db,
            username,
            updated_by=user.username,
            new_work_email=payload.work_email,
            new_preferred_name=payload.preferred_name,
            new_manager_username=payload.manager_username,
            new_is_active=payload.is_active,
        )
    except EmployeeUpdateError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc
    if not entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=` whitelist | Update Employee | [put_employees_{username}.md](put_employees_{username}.md) |
| POST | /employees/{username}/deactivate | `)
    entry = employee_crud.deactivate_employee(db, username, deactivated_by=user.username)
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=` whitelist | Deactivate Employee | [post_employees_{username}_deactivate.md](post_employees_{username}_deactivate.md) |
| POST | /employees/{username}/reactivate | `)
    entry = employee_crud.reactivate_employee(db, username, reactivated_by=user.username)
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=` whitelist | Reactivate Employee | [post_employees_{username}_reactivate.md](post_employees_{username}_reactivate.md) |
