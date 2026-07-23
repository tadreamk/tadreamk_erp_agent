# Personal Particular API

Base prefixes:
- `/personal-particular`
- `/personal-particulars`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /personal-particular/me | Authenticated employee | Get Me | [get_personal-particular_me.md](get_personal-particular_me.md) |
| GET | /personal-particulars/ | `)
    rows, total = personal_particular_queries.list_personal_particulars_left_join_employee(
        db,
        search=search,
        include_inactive=include_inactive,
        page=page,
        limit=limit,
    )
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=` whitelist | List Personal Particulars | [get_personal-particulars_.md](get_personal-particulars_.md) |
| POST | /personal-particulars/ | `)
    try:
        entry = personal_particular_write_ops.create_personal_particular(
            db,
            username=username,
            created_by=user.username,
            fields=payload.model_dump(exclude_unset=True),
        )
    except PersonalParticularCreateError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc
    return APIResponse(
        success=True,
        message=` whitelist | Create Personal Particular | [post_personal-particulars_.md](post_personal-particulars_.md) |
| DELETE | /personal-particulars/{username} | `)
    removed = personal_particular_write_ops.delete_personal_particular(db, username)
    if not removed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f` whitelist | Delete Personal Particular | [delete_personal-particulars_{username}.md](delete_personal-particulars_{username}.md) |
| GET | /personal-particulars/{username} | `)
    entry = get_personal_particular_or_404_by_username(db, username)
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=f` whitelist | Get Personal Particular | [get_personal-particulars_{username}.md](get_personal-particulars_{username}.md) |
| PUT | /personal-particulars/{username} | `)
    entry = personal_particular_write_ops.update_personal_particular(
        db,
        username,
        updated_by=user.username,
        fields=payload.model_dump(exclude_unset=True),
    )
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f` whitelist | Update Personal Particular | [put_personal-particulars_{username}.md](put_personal-particulars_{username}.md) |
