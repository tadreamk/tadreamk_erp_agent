# Leave API

Base prefixes:
- `/leave`
- `/leave/me`
- `/leave/requests`
- `/leave/team`
- `/leave/team/requests/{request_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /leave/all | `)
    rows, total = leave_crud.find_all(
        db,
        status_filter=status_filter,
        leave_type=leave_type,
        employee_username=employee_username,
        manager_username=manager_username,
        from_date=_parse_date(from_date),
        to_date=_parse_date(to_date),
        page=page,
        limit=limit,
    )
    return {
        ` whitelist | List All Requests | [get_leave_all.md](get_leave_all.md) |
| GET | /leave/calendar | Authenticated employee | List Calendar Events | [get_leave_calendar.md](get_leave_calendar.md) |
| GET | /leave/me/balance | Authenticated employee | Get My Balance | [get_leave_me_balance.md](get_leave_me_balance.md) |
| GET | /leave/me/requests | Authenticated employee | List My Requests | [get_leave_me_requests.md](get_leave_me_requests.md) |
| POST | /leave/me/requests | Authenticated employee | Submit My Request | [post_leave_me_requests.md](post_leave_me_requests.md) |
| GET | /leave/requests/{request_id} | Authenticated | Get Request Detail | [get_leave_requests_{request_id}.md](get_leave_requests_{request_id}.md) |
| GET | /leave/team/requests | Authenticated employee | List Team Requests | [get_leave_team_requests.md](get_leave_team_requests.md) |
| POST | /leave/team/requests/{request_id}/approve | Authenticated employee | Approve Team Request | [post_leave_team_requests_{request_id}_approve.md](post_leave_team_requests_{request_id}_approve.md) |
| POST | /leave/team/requests/{request_id}/reject | Authenticated employee | Reject Team Request | [post_leave_team_requests_{request_id}_reject.md](post_leave_team_requests_{request_id}_reject.md) |
