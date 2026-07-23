# Audit Log API

Base prefixes:
- `/audit-log`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /audit-log/ | `)
    rows, total = audit_log_queries.list_audit_log_paginated(
        db,
        caller_username=caller_username,
        target_username=target_username,
        endpoint=endpoint,
        occurred_after=occurred_after,
        occurred_before=occurred_before,
        page=page,
        limit=limit,
    )
    usernames: set[str] = set()
    for row in rows:
        if row.caller_username:
            usernames.add(row.caller_username)
        if row.target_username:
            usernames.add(row.target_username)
    employees_by_username = (
        employee_queries.find_employees_by_usernames(db, list(usernames)) if usernames else {}
    )
    return {
        ` whitelist | List Audit Log | [get_audit-log_.md](get_audit-log_.md) |
| GET | /audit-log/stats | `)
    by_endpoint = audit_log_queries.count_by_endpoint(
        db, occurred_after=occurred_after, occurred_before=occurred_before
    )
    return {` whitelist | Get Audit Log Stats | [get_audit-log_stats.md](get_audit-log_stats.md) |
