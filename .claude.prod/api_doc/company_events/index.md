# Company Events API

Base prefixes:
- `/calendar`
- `/calendar/company-events`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /calendar/company-events | Authenticated employee | List Company Events In Window | [get_calendar_company-events.md](get_calendar_company-events.md) |
| POST | /calendar/company-events | Authenticated | Create Company Event | [post_calendar_company-events.md](post_calendar_company-events.md) |
| GET | /calendar/company-events/employees | Authenticated | List Employees For Picker | [get_calendar_company-events_employees.md](get_calendar_company-events_employees.md) |
| GET | /calendar/company-events/list | Authenticated | List Company Events Paginated | [get_calendar_company-events_list.md](get_calendar_company-events_list.md) |
| DELETE | /calendar/company-events/{event_id} | Authenticated | Delete Company Event | [delete_calendar_company-events_{event_id}.md](delete_calendar_company-events_{event_id}.md) |
| GET | /calendar/company-events/{event_id} | Authenticated employee | Get Company Event | [get_calendar_company-events_{event_id}.md](get_calendar_company-events_{event_id}.md) |
| PUT | /calendar/company-events/{event_id} | Authenticated | Update Company Event | [put_calendar_company-events_{event_id}.md](put_calendar_company-events_{event_id}.md) |
