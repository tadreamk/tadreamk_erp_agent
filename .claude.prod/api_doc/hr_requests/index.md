# HR Requests API

Base prefixes:
- `/hr-requests`
- `/hr-requests/all`
- `/hr-requests/me`
- `/hr-requests/me/{request_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /hr-requests/all | `)
    rows, total = hr_request_service.list_all_requests(
        db,
        status_filter=status_filter,
        q=q,
        page=page,
        limit=limit,
    )
    return {
        ` whitelist | List All Requests | [get_hr-requests_all.md](get_hr-requests_all.md) |
| GET | /hr-requests/all/{request_id} | `)
    row = get_hr_request_or_404(db, request_id)
    return APIResponse(
        success=True,
        message=` whitelist | Get Request For Oversight | [get_hr-requests_all_{request_id}.md](get_hr-requests_all_{request_id}.md) |
| GET | /hr-requests/me | Authenticated employee | List My Requests | [get_hr-requests_me.md](get_hr-requests_me.md) |
| POST | /hr-requests/me | Authenticated employee | Submit Request | [post_hr-requests_me.md](post_hr-requests_me.md) |
| POST | /hr-requests/me/attachments | Authenticated employee | Upload Attachment | [post_hr-requests_me_attachments.md](post_hr-requests_me_attachments.md) |
| GET | /hr-requests/me/{request_id} | Authenticated employee | Get My Request | [get_hr-requests_me_{request_id}.md](get_hr-requests_me_{request_id}.md) |
| POST | /hr-requests/me/{request_id}/finish | Authenticated employee | Mark Finished | [post_hr-requests_me_{request_id}_finish.md](post_hr-requests_me_{request_id}_finish.md) |
