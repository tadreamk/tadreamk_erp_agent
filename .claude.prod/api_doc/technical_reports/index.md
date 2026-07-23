# Technical Reports API

Base prefixes:
- `/technical-reports`
- `/technical-reports/all`
- `/technical-reports/all/{report_id}`
- `/technical-reports/me`
- `/technical-reports/me/{report_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /technical-reports/all | Authenticated | List All Reports | [get_technical-reports_all.md](get_technical-reports_all.md) |
| GET | /technical-reports/all/{report_id} | Authenticated | Get Report For Oversight | [get_technical-reports_all_{report_id}.md](get_technical-reports_all_{report_id}.md) |
| POST | /technical-reports/all/{report_id}/resolve | Authenticated | Mark Resolved Admin | [post_technical-reports_all_{report_id}_resolve.md](post_technical-reports_all_{report_id}_resolve.md) |
| GET | /technical-reports/me | Authenticated employee | List My Reports | [get_technical-reports_me.md](get_technical-reports_me.md) |
| POST | /technical-reports/me | Authenticated employee | Submit Report | [post_technical-reports_me.md](post_technical-reports_me.md) |
| POST | /technical-reports/me/attachments | Authenticated employee | Upload Attachment | [post_technical-reports_me_attachments.md](post_technical-reports_me_attachments.md) |
| GET | /technical-reports/me/{report_id} | Authenticated employee | Get My Report | [get_technical-reports_me_{report_id}.md](get_technical-reports_me_{report_id}.md) |
| PUT | /technical-reports/me/{report_id} | Authenticated employee | Edit My Report | [put_technical-reports_me_{report_id}.md](put_technical-reports_me_{report_id}.md) |
| POST | /technical-reports/me/{report_id}/resolve | Authenticated employee | Mark Resolved Self | [post_technical-reports_me_{report_id}_resolve.md](post_technical-reports_me_{report_id}_resolve.md) |
