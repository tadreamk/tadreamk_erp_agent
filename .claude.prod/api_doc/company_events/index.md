# Company Events API

Manage company-wide events with calendar integration and participant notifications.

**Access control:**
- All authenticated employees can view events (`GET` endpoints).
- Creating, updating, and deleting events requires `company-events` whitelist.

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/company-events/calendar` | Get events for calendar display | [get_company-events_calendar.md](./get_company-events_calendar.md) |
| `GET` | `/company-events/employees` | Get employees for participant picker (whitelist) | [get_company-events_employees.md](./get_company-events_employees.md) |
| `GET` | `/company-events` | List all company events | [get_company-events.md](./get_company-events.md) |
| `GET` | `/company-events/{event_id}` | Get company event details | [get_company-events_{event_id}.md](./get_company-events_{event_id}.md) |
| `POST` | `/company-events` | Create a new company event (whitelist) | [post_company-events.md](./post_company-events.md) |
| `PUT` | `/company-events/{event_id}` | Update a company event (whitelist) | [put_company-events_{event_id}.md](./put_company-events_{event_id}.md) |
| `DELETE` | `/company-events/{event_id}` | Soft delete a company event (whitelist) | [delete_company-events_{event_id}.md](./delete_company-events_{event_id}.md) |
