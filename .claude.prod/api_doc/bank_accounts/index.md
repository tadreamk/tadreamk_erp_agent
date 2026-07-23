# Bank Accounts API

Base prefixes:
- `/bank-account`
- `/bank-accounts`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /bank-account/me | Authenticated employee | Get Me | [get_bank-account_me.md](get_bank-account_me.md) |
| GET | /bank-accounts/ | `)
    rows, total = bank_account_queries.list_bank_accounts_left_join_employee(
        db, search=search, page=page, limit=limit
    )
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=` whitelist | List Bank Accounts | [get_bank-accounts_.md](get_bank-accounts_.md) |
| DELETE | /bank-accounts/{username} | `)
    removed = bank_account_write_ops.delete_bank_account(db, username)
    if not removed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f` whitelist | Delete Bank Account | [delete_bank-accounts_{username}.md](delete_bank-accounts_{username}.md) |
| GET | /bank-accounts/{username} | `)
    entry = get_bank_account_or_404_by_username(db, username)
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=f` whitelist | Get Bank Account | [get_bank-accounts_{username}.md](get_bank-accounts_{username}.md) |
| PUT | /bank-accounts/{username} | `)
    try:
        entry = bank_account_write_ops.upsert_bank_account(
            db,
            username=username,
            actor_username=user.username,
            fields=payload.model_dump(exclude_unset=True),
        )
    except BankAccountWriteError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc
    audit_names = resolve_audit_pair_names(
        db,
        created_by=entry.created_by,
        updated_by=entry.updated_by,
    )
    return APIResponse(
        success=True,
        message=` whitelist | Upsert Bank Account | [put_bank-accounts_{username}.md](put_bank-accounts_{username}.md) |
